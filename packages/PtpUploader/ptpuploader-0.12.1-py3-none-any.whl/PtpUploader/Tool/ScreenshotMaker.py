import contextlib
import functools
import os
import shutil
import tempfile

from PtpUploader import ImageHost
from PtpUploader.PtpUploaderException import PtpUploaderException
from PtpUploader.Settings import Settings, config
from PtpUploader.Tool import Oxipng, ImageMagick
from PtpUploader.Tool.Ffmpeg import Ffmpeg
from PtpUploader.Tool.Mplayer import Mplayer
from PtpUploader.Tool.Mpv import Mpv
from PtpUploader.Tool.LibMpv import LibMpv


# Blatantly stolen from https://stackoverflow.com/a/57701186
@contextlib.contextmanager
def temporary_filename(suffix=None):
    """Context that introduces a temporary file.

    Creates a temporary file, yields its name, and upon context exit, deletes it.
    (In contrast, tempfile.NamedTemporaryFile() provides a 'file' object and
    deletes the file as soon as that file object is closed, so the temporary file
    cannot be safely re-opened by another library or process.)

    Args:
      suffix: desired filename extension (e.g. '.mp4').

    Yields:
      The name of the temporary file.
    """
    try:
        f = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        tmp_name = f.name
        f.close()
        yield tmp_name
    finally:
        os.unlink(tmp_name)


class ScreenshotMaker:
    def __init__(self, logger, inputVideoPath):
        self.Logger = logger

        self.InternalScreenshotMaker = None

        if config.tools.screenshot_tool == "mpv":
            self.InternalScreenshotMaker = Mpv(logger, inputVideoPath)
        elif config.tools.screenshot_tool == "libmpv":
            self.InternalScreenshotMaker = LibMpv(logger, inputVideoPath)
        elif config.tools.screenshot_tool == "ffmpeg":
            self.InternalScreenshotMaker = Ffmpeg(logger, inputVideoPath)
        elif config.tools.screenshot_tool == "mplayer":
            self.InternalScreenshotMaker = Mplayer(logger, inputVideoPath)
        else:
            if Settings.MpvPath and shutil.which(Settings.MpvPath):
                self.InternalScreenshotMaker = Mpv(logger, inputVideoPath)
            elif Settings.FfmpegPath and shutil.which(Settings.FfmpegPath):
                self.InternalScreenshotMaker = Ffmpeg(logger, inputVideoPath)
            elif Settings.MplayerPath and shutil.which(Settings.MplayerPath):
                self.InternalScreenshotMaker = Mplayer(logger, inputVideoPath)
        if self.InternalScreenshotMaker is None:
            raise PtpUploaderException("No screenshot tool found")

    def GetScaleSize(self):
        return self.InternalScreenshotMaker.ScaleSize

    # Returns with the URL of the uploaded image.
    def __TakeAndUploadScreenshot(self, timeInSeconds):
        with temporary_filename(".png") as outputPngPath:
            self.InternalScreenshotMaker.MakeScreenshotInPng(
                timeInSeconds, outputPngPath
            )

            # Always convert with imagemagick, even if it's not used for compression
            imagemagick_exists = config.tools.imagemagick.path and shutil.which(
                config.tools.imagemagick.path
            )
            if imagemagick_exists:
                ImageMagick.convert_8bit(outputPngPath)

            if config.tools.oxipng.path and shutil.which(config.tools.oxipng.path):
                Oxipng.optimize_png(outputPngPath)
            elif imagemagick_exists:
                ImageMagick.optimize_png(outputPngPath)

            imageUrl = ImageHost.upload(self.Logger, imagePath=outputPngPath)

        return imageUrl

    # Takes maximum five screenshots from the first 30% of the video.
    # Returns with the URLs of the uploaded images.
    def TakeAndUploadScreenshots(
        self, outputImageDirectory, durationInSec, numberOfScreenshotsToTake
    ):
        urls = []

        if numberOfScreenshotsToTake > config.uploader.max_screenshots:
            numberOfScreenshotsToTake = config.uploader.max_screenshots

        for i in range(numberOfScreenshotsToTake):
            position = 0.10 + (i * 0.05)
            urls.append(self.__TakeAndUploadScreenshot(int(durationInSec * position)))

        return urls

    # We sort video files by their size (less than 50 MB difference is ignored) and by their name.
    # Sorting by name is needed to ensure that the screenshot is taken from the first video to avoid spoilers when a release contains multiple videos.
    # Sorting by size is needed to ensure that we don't take the screenshots from the sample or extras included.
    # Ignoring less than 50 MB difference is needed to make sure that CD1 will be sorted before CD2 even if CD2 is larger than CD1 by 49 MB.
    @staticmethod
    def SortVideoFiles(files):
        class SortItem:
            def __init__(self, path):
                self.Path = path
                self.LowerPath = str(path).lower()
                self.Size = os.path.getsize(path)

            @staticmethod
            def Compare(item1, item2):
                ignoreSizeDifference = 50 * 1024 * 1024
                sizeDifference = item1.Size - item2.Size
                if abs(sizeDifference) > ignoreSizeDifference:
                    if item1.Size > item2.Size:
                        return -1
                    else:
                        return 1

                if item1.LowerPath < item2.LowerPath:
                    return -1
                elif item1.LowerPath > item2.LowerPath:
                    return 1
                else:
                    return 0

        filesToSort = []
        for file in files:
            item = SortItem(file)
            filesToSort.append(item)

        filesToSort.sort(key=functools.cmp_to_key(SortItem.Compare))

        files = []
        for item in filesToSort:
            files.append(item.Path)

        return files
