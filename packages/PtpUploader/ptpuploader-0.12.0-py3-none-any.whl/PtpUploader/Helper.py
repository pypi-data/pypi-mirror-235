import os
import re
import time

from datetime import timedelta
from pathlib import Path
from typing import List, Tuple

import bencode
import requests

from PtpUploader.MyGlobals import MyGlobals
from PtpUploader.PtpUploaderException import PtpUploaderException


def GetIdxSubtitleLanguages(path: str):
    languages = []

    # id: en, index: 0
    languageRe = re.compile(r"id: ([a-z][a-z]), index: \d+$", re.IGNORECASE)

    # U is needed for "universal" newline support: to handle \r\n as \n.
    with open(path) as pathHandle:
        for line in pathHandle.readlines():
            match = languageRe.match(line)
            if match is not None:
                languages.append(match.group(1))

    return languages


# Supported formats: "100 GB", "100 MB", "100 bytes". (Space is optional.)
# Returns with an integer.
# Returns with 0 if size can't be found.
def GetSizeFromText(text: str):
    text = text.replace(" ", "").replace(
        ",", ""
    )  # For sizes like this: 1,471,981,530bytes
    text = text.replace("GiB", "GB").replace("MiB", "MB")

    matches = re.match("(.+)GB", text)
    if matches is not None:
        return int(float(matches.group(1)) * 1024 * 1024 * 1024)

    matches = re.match("(.+)MB", text)
    if matches is not None:
        return int(float(matches.group(1)) * 1024 * 1024)

    matches = re.match("(.+)bytes", text)
    if matches is not None:
        return int(matches.group(1))

    return 0


def SizeToText(size: int):
    if size < 1024 * 1024 * 1024:
        return "%.2f MiB" % (float(size) / (1024 * 1024))
    return "%.2f GiB" % (float(size) / (1024 * 1024 * 1024))


# timeDifference must be datetime.timedelta.
def TimeDifferenceToText(
    td: timedelta, levels: int = 2, agoText=" ago", noDifferenceText="Just now"
) -> str:
    data = {}
    data["y"], seconds = divmod(int(td.total_seconds()), 31556926)
    # 2629744 seconds = ~1 month (The mean month length of the Gregorian calendar is 30.436875 days.)
    data["mo"], seconds = divmod(seconds, 2629744)
    data["d"], seconds = divmod(seconds, 86400)
    data["h"], seconds = divmod(seconds, 3600)
    data["m"], data["s"] = divmod(seconds, 60)

    time_parts = [f"{round(value)}{name}" for name, value in data.items() if value > 0]
    if time_parts:
        return "".join(time_parts[:levels]) + agoText
    return noDifferenceText


def MakeRetryingHttpGetRequestWithRequests(
    url: str, maximumTries=3, delayBetweenRetriesInSec=10
):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
    }

    while True:
        try:
            result = MyGlobals.session.get(url, headers=headers)
            result.raise_for_status()
            return result
        except requests.exceptions.ConnectionError:
            if maximumTries > 1:
                maximumTries -= 1
                time.sleep(delayBetweenRetriesInSec)
            else:
                raise


def MakeRetryingHttpPostRequestWithRequests(
    url: str, postData, maximumTries=3, delayBetweenRetriesInSec=10
):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
    }

    while True:
        try:
            result = MyGlobals.session.post(url, data=postData, headers=headers)
            result.raise_for_status()
            return result
        except requests.exceptions.ConnectionError:
            if maximumTries > 1:
                maximumTries -= 1
                time.sleep(delayBetweenRetriesInSec)
            else:
                raise


# Path can be a file or a directory. (Obviously.)
def GetPathSize(path) -> int:
    path = Path(path).resolve()
    if path.is_file():
        return path.stat().st_size

    return sum(p.stat().st_size for p in path.rglob("*"))


# Always uses / as path separator.
def GetFileListFromTorrent(torrentPath) -> List[str]:
    with open(torrentPath, "rb") as fh:
        data = bencode.decode(fh.read())
    name = data["info"].get("name", None)
    files = data["info"].get("files", None)

    if files is None:
        return [name]

    fileList = []
    for fileInfo in files:
        path = "/".join(fileInfo["path"])
        fileList.append(path)

    return fileList


def RemoveDisallowedCharactersFromPath(text: str) -> str:
    newText = text

    # These characters can't be in filenames on Windows.
    forbiddenCharacters = r"""\/:*?"<>|"""
    for c in forbiddenCharacters:
        newText = newText.replace(c, "")

    newText = newText.strip()

    if len(newText) > 0:
        return newText
    raise PtpUploaderException("New name for '%s' resulted in empty string." % text)


def ValidateTorrentFile(torrentPath):
    try:
        with open(torrentPath, "rb") as fh:
            bencode.decode(fh.read())
            return True
    except Exception as e:
        raise PtpUploaderException(
            "File '%s' is not a valid torrent." % torrentPath
        ) from e


def GetSuggestedReleaseNameAndSizeFromTorrentFile(torrentPath) -> Tuple[str, int]:
    with open(torrentPath, "rb") as fh:
        data = bencode.decode(fh.read())
    name = data["info"].get("name", None)
    files = data["info"].get("files", None)
    if files is None:
        # It is a single file torrent, remove the extension.
        name, _ = os.path.splitext(name)
        size = data["info"]["length"]
        return name, size
    size = 0
    for file in files:
        size += file["length"]

    return name, size


def DecodeHtmlEntities(html):
    return html.unescape(html)
