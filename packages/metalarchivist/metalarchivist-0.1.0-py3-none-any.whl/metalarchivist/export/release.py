
import os
import time
import pathlib

from datetime import datetime

import urllib3

from .type import MetalArchivesDirectory, ReleasePage, ReleasePages, normalize_keyword_casing


__FILE_DIRECTORY__ = pathlib.Path(__file__).relative_to(os.getcwd()) \
                                           .parent.resolve() \
                                           .as_posix()


class Releases:

    @staticmethod
    def get_upcoming(echo=0, page_size=100, wait=.1) -> ReleasePage:
        data = ReleasePages()
        record_cursor = 0
        timeout = urllib3.Timeout(connect=3.0, read=9.0)

        while True:
            endpoint = MetalArchivesDirectory.upcoming_releases(echo, record_cursor, page_size)
            response = urllib3.request('GET', endpoint, timeout=timeout).json()
            releases = ReleasePage(**normalize_keyword_casing(response))

            data.append(releases)

            record_cursor += page_size
            echo += 1

            if releases.total_records - 1 > record_cursor:
                time.sleep(wait)
                continue
            break

        return data.combine()

    @staticmethod
    def get_all():
        raise NotImplementedError

    @staticmethod
    def get_range(range_start: datetime, range_stop: datetime | None = None,
                  echo=0, page_size=100, wait=.1) -> ReleasePage:

        data = ReleasePages()
        record_cursor = 0
        timeout = urllib3.Timeout(connect=3.0, read=9.0)

        range_stop_str = range_stop.strftime('%Y-%m-%d') if range_stop is not None else '0000-00-00'

        while True:
            endpoint = MetalArchivesDirectory.upcoming_releases(echo, record_cursor, page_size,
                                                                range_start.strftime('%Y-%m-%d'),
                                                                range_stop_str)
            response = urllib3.request('GET', endpoint, timeout=timeout).json()
            releases = ReleasePage(**normalize_keyword_casing(response))

            data.append(releases)

            record_cursor += page_size
            echo += 1

            if releases.total_records - 1 > record_cursor:
                time.sleep(wait)
                continue
            break

        return data.combine()
