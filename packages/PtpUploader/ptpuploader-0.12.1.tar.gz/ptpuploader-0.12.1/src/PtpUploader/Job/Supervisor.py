"""Replaces the artisanal (but impressive) python 2 threading system
This directly handles:
- Loading announcement files
- Scanning the DB for work
- Watching the client for pending downloads
All of these actions will happen on a schedule, but the thread can be woken up immediately by an Event.

For WorkerBase actions, they get launched into a ThreadPoolExecutor, with an event flag
to allow for interrupting the work phases. This allows this class to check the status of
any active futures when deciding how to handle start/stop requests.

However, there is no direct locking of resources, as we can use the DB
as more flexible thread-safe state holder.

It's called the JobSupervisor because supervisors are better than managers.

"""

import logging
import queue
import threading
import traceback

from concurrent import futures
from typing import Dict, List

from django.db.models import Q  # type: ignore
from django.utils import timezone  # type: ignore
from pyrosimple.util.rpc import HashNotFound

from PtpUploader.Job import LoadFile
from PtpUploader.Job.CheckAnnouncement import CheckAnnouncement
from PtpUploader.Job.Delete import Delete
from PtpUploader.Job.Upload import Upload
from PtpUploader.PtpUploaderMessage import *
from PtpUploader.ReleaseInfo import ReleaseInfo
from PtpUploader.Settings import config


logger = logging.getLogger(__name__)


class JobSupervisor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.futures: Dict[str, List[threading.Event, futures.Future]] = {}
        self.message_queue: queue.SimpleQueue = queue.SimpleQueue()
        self.stop_requested: threading.Event = threading.Event()
        self.pool: futures.ThreadPoolExecutor = futures.ThreadPoolExecutor(
            max_workers=config.workers.threads
        )

    def __repr__(self):
        running = []
        done = []
        waiting = []
        for key, val in self.futures.items():
            _, future = val
            if future.running():
                running.append(key)
            elif future.done():
                done.append(key)
            else:
                waiting.append(key)
        return f"running: {running}, waiting: {waiting}, done: {done}"

    def check_pending_downloads(self):
        for release in ReleaseInfo.objects.filter(
            JobRunningState=ReleaseInfo.JobState.InDownload
        ):
            try:
                release.AnnouncementSource.IsDownloadFinished(logger, release)
            except HashNotFound as e:
                release.ErrorMessage = str(e)
                release.JobRunningState = ReleaseInfo.JobState.Failed
                release.save()
                continue
            if (
                release.Id not in self.futures
                and release.AnnouncementSource.IsDownloadFinished(logger, release)
            ):
                logger.info("Launching upload job for %s", release.Id)
                worker_stop_flag = threading.Event()
                worker = Upload(release_id=release.Id, stop_requested=worker_stop_flag)
                self.futures[release.Id] = [
                    worker_stop_flag,
                    self.pool.submit(worker.Work),
                ]

    def load_announcements(self):
        LoadFile.scan_dir()

    def add_message(self, message):
        if isinstance(message, PtpUploaderMessageBase):
            self.message_queue.put(message)
        else:
            logger.warning("Unknown message '%s'", message)

    def delete_job(self, r_id, mode):
        if r_id in self.futures:
            return  # Don't muck with an active job
        worker_stop_flag = threading.Event()
        worker = Delete(release_id=r_id, mode=mode, stop_requested=worker_stop_flag)
        self.futures[r_id] = [
            worker_stop_flag,
            self.pool.submit(worker.Work),
        ]

    def scan_db(self):
        """Find releases pending work by their DB status"""
        for release in ReleaseInfo.objects.filter(
            Q(JobRunningState=ReleaseInfo.JobState.WaitingForStart)
            | (
                Q(ScheduleTime__lte=timezone.now())
                & Q(JobRunningState=ReleaseInfo.JobState.Scheduled)
            )
        ):
            if release.Id not in self.futures:
                logger.info("Launching check job for %s", release.Id)
                worker_stop_flag = threading.Event()
                worker = CheckAnnouncement(
                    release_id=release.Id, stop_requested=worker_stop_flag
                )
                self.futures[release.Id] = [
                    worker_stop_flag,
                    self.pool.submit(worker.Work),
                ]

    def process_pending(self):
        self.check_pending_downloads()
        self.load_announcements()
        self.scan_db()

    def stop_future(self, release_id):
        release = ReleaseInfo.objects.get(Id=release_id)
        if release.Id in self.futures:
            pass
        elif release.JobRunningState in [
            ReleaseInfo.JobState.InDownload,
            ReleaseInfo.JobState.Scheduled,
        ]:
            release.JobRunningState = ReleaseInfo.JobState.Paused
            release.save()

    def reap_finished(self):
        for key, val in list(self.futures.items()):
            _, result = val
            if result.done():
                if result.exception():
                    logger.info(  # Exceptions are used as messengers, hence info
                        "Job %s finished with exception '%s'", key, result.exception()
                    )
                del self.futures[key]

    def work(self):
        if self.futures.keys():
            logger.info(repr(self))
        try:
            message = self.message_queue.get(timeout=3)
            if isinstance(message, PtpUploaderMessageStopJob):
                self.stop_future(message.ReleaseInfoId)
            elif isinstance(message, PtpUploaderMessageStartJob):
                pass  # Just wake up the thread to scan the db
            elif isinstance(message, PtpUploaderMessageDeleteJob):
                self.delete_job(message.ReleaseInfoId, message.mode)
            elif isinstance(message, PtpUploaderMessageQuit):
                self.stop_requested.set()
        except queue.Empty:
            pass

        if self.stop_requested.is_set():
            self.reap_finished()
            self.cleanup_futures()
            return True
        self.reap_finished()
        self.process_pending()
        return None

    def run(self):
        logger.info("Starting supervisors")
        while True:
            try:
                if self.work() is not None:
                    break
            except (KeyboardInterrupt, SystemExit):
                logger.info("Received system interrupt")
                self.add_message(PtpUploaderMessageQuit())
            except Exception as e:
                print(traceback.print_exc())
                logger.info("Received exception %s, attempting to continue", e)

    def cleanup_futures(self):
        pass
