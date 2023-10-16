
import os
import unittest

from datetime import datetime
from configparser import ConfigParser

import pandas as pd

from .util import Submodule, prepare_submodule, run_test_cases


class TestMetalArchivesDirectory(unittest.TestCase):

    def test_releases_endpoint(self):
        export = prepare_submodule(Submodule.EXPORT)

        self.assertIsNotNone(export)
        
        self.assertIn('MetalArchivesDirectory', dir(export))

        range_start = datetime(1990, 1, 1).strftime('%Y-%m-%d')
        range_stop = datetime(1990, 12, 31).strftime('%Y-%m-%d')

        self.assertEqual(range_start, '1990-01-01')
        self.assertEqual(range_stop, '1990-12-31')

        expected_endpoint = ('https://www.metal-archives.com/release/ajax-upcoming/json/1'
                             '?sEcho=0&iDisplayStart=0&iDisplayLength=100'
                             '&fromDate=1990-01-01&toDate=1990-12-31')

        endpoint_query = dict(from_date=range_start, to_date=range_stop)
        actual_endpoint = export.MetalArchivesDirectory.upcoming_releases(**endpoint_query)

        self.assertEqual(expected_endpoint, actual_endpoint)


class TestReleases(unittest.TestCase):

    def test_releases(self):
        export = prepare_submodule(Submodule.EXPORT)
        
        self.assertIn('Releases', dir(export))

        upcoming_component_attributes = dir(export.Releases)
        self.assertIn('get_all', upcoming_component_attributes)
        self.assertIn('get_upcoming', upcoming_component_attributes)
        self.assertIn('get_range', upcoming_component_attributes)

    def test_release_fields(self):
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)
        
        releases = export.Releases.get_upcoming()

        releases_attributes = dir(releases)
        self.assertIn('total_records', releases_attributes)
        self.assertIn('total_display_records', releases_attributes)
        self.assertIn('echo', releases_attributes)
        self.assertIn('data', releases_attributes)

        self.assertIsInstance(releases.total_records, int)
        self.assertIsInstance(releases.total_display_records, int)
        self.assertIsInstance(releases.echo, int)
        self.assertIsInstance(releases.data, list)

        self.assertEqual(releases.total_records, releases.total_display_records)
        self.assertEqual(releases.echo, 0)

    def test_upcoming(self):
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        releases = export.Releases.get_upcoming()
        self.assertIsNotNone(releases)
        self.assertIsInstance(releases, export.ReleasePage)

        data = releases.data
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), releases.total_records)

        album_release = data.pop()
        self.assertIsInstance(album_release, export.AlbumRelease)

    def test_range(self):
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Releases', dir(export))

        releases = export.Releases.get_range(datetime(1990, 1, 1), datetime(1990, 12, 31))
        self.assertIsNotNone(releases)
        self.assertIsInstance(releases, export.ReleasePage)

        total_records = releases.total_records
        total_display_records = releases.total_display_records
        self.assertEqual(total_records, total_display_records)

        self.assertEqual(releases.echo, 0)

        data = releases.data
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), total_records)

        album_release = data.pop()
        self.assertIsInstance(album_release, export.AlbumRelease)

    def test_range_with_null_upper_bound(self):
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Releases', dir(export))

        releases = export.Releases.get_range(datetime(2023, 8, 11))
        self.assertIsNotNone(releases)
        self.assertIsInstance(releases, export.ReleasePage)

        total_records = releases.total_records
        total_display_records = releases.total_display_records
        self.assertEqual(total_records, total_display_records)

        self.assertEqual(releases.echo, 0)

        data = releases.data
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), total_records)

        album_release = data.pop()
        self.assertIsInstance(album_release, export.AlbumRelease)

    def test_album_release(self):
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Releases', dir(export))

        releases = export.Releases.get_range(datetime(2023, 8, 11))

        data = releases.data
        self.assertIsInstance(data, list)

        # can be greater than total records due to split albums
        self.assertGreaterEqual(len(data), releases.total_records)

        album_release = data.pop()
        self.assertIsInstance(album_release, export.AlbumRelease)

        self.assertIn('release_type', dir(album_release))
        self.assertIn('genres', dir(album_release))
        self.assertIn('release_date', dir(album_release))
        self.assertIn('added_date', dir(album_release))
        self.assertIn('band', dir(album_release))
        self.assertIn('album', dir(album_release))

        self.assertIsInstance(album_release.genres, export.Genres)

        self.assertIsInstance(album_release.release_date, datetime)
        self.assertIsInstance(album_release.added_date, datetime)

        self.assertIsInstance(album_release.band, export.BandLink)
        self.assertIsInstance(album_release.album, export.AlbumLink)

    def test_release_report(self):
        config = ConfigParser({'unittests': {'OUTPUTDIR': './'}})
        config.read('metallum.cfg')
        
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        report = prepare_submodule(Submodule.REPORT)
        self.assertIsNotNone(report)

        releases = report.get_releases()
        self.assertIsInstance(releases, pd.DataFrame)

        output_path = os.path.join(config['unittests']['OUTPUTDIR'], 'releases-upcoming.csv')
        releases.to_csv(output_path, index=False)

        releases = report.get_releases(datetime(2023, 1, 1))
        self.assertIsInstance(releases, pd.DataFrame)

        output_path = os.path.join(config['unittests']['OUTPUTDIR'], 'releases-2023-YTD.csv')
        releases.to_csv(output_path, index=False)

if __name__ == '__main__':
    run_test_cases()
