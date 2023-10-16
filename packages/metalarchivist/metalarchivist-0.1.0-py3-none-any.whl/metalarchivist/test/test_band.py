
import os
import unittest

from configparser import ConfigParser

import pandas as pd

from .util import Submodule, prepare_submodule, run_test_cases



class TestBands(unittest.TestCase):
    def test_band_report(self):
        config = ConfigParser({'unittests': {'OUTPUTDIR': './'}})
        config.read('metallum.cfg')

        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        report = prepare_submodule(Submodule.REPORT)
        self.assertIsNotNone(report)

        bands = report.get_bands(['https://www.metal-archives.com/bands/Furia/23765',
                                  'https://www.metal-archives.com/bands/Cult_of_Fire/3540334368',
                                  'https://www.metal-archives.com/bands/Urfaust/19596',
                                  'https://www.metal-archives.com/bands/A_Forest_of_Stars/115504',
                                  'https://www.metal-archives.com/bands/Burzum/88',
                                  'https://www.metal-archives.com/bands/Mayhem/67',
                                  'https://www.metal-archives.com/bands/Satanic_Warmaster/989'])

        self.assertIsInstance(bands, pd.DataFrame)
        
        output_path = os.path.join(config['unittests']['OUTPUTDIR'], 'test-bands.csv')
        bands.to_csv(output_path, index=False)

    def test_genres(self):

        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        genres = export.Genres('Drone/Doom Metal (early); Psychedelic/Post-Rock (later)')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 4)
        self.assertEqual(genres.clean_genre, 'Doom, Drone, Post-Rock, Psychedelic')

        genres = export.Genres('Progressive Doom/Post-Metal')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 3)
        self.assertEqual(genres.clean_genre, 'Doom, Post-Metal, Progressive')

        genres = export.Genres('Blackened Death Metal/Grindcore')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 3)
        self.assertEqual(genres.clean_genre, 'Blackened, Death, Grindcore')

        genres = export.Genres('Black Metal')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 1)
        self.assertEqual(genres.clean_genre, 'Black')

        genres = export.Genres('Progressive Death/Black Metal')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 3)
        self.assertEqual(genres.clean_genre, 'Black, Death, Progressive')

        genres = export.Genres('Epic Black Metal')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 2)
        self.assertEqual(genres.clean_genre, 'Black, Epic')

        genres = export.Genres('Various (early); Atmospheric Black Metal, Ambient (later)')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 4)
        self.assertEqual(genres.clean_genre, 'Various, Ambient, Atmospheric, Black')

        genres = export.Genres('Symphonic Gothic Metal with Folk influences')
        self.assertIsNotNone(genres)
        self.assertEqual(len(genres.phases), 3)
        self.assertEqual(genres.clean_genre, 'Folk, Gothic, Symphonic')

    def test_band_profile(self):
        
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Band', dir(export))

        band = export.Band.get_profile('https://www.metal-archives.com/bands/Furia/23765')
        self.assertEqual(band.name, 'Furia')
        self.assertEqual(band.metallum_id, 23765)

    def test_band_profiles(self):
        
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Band', dir(export))

        bands = export.Band.get_profiles(['https://www.metal-archives.com/bands/Furia/23765',
                                          'https://www.metal-archives.com/bands/Cult_of_Fire/3540334368',
                                          'https://www.metal-archives.com/bands/Urfaust/19596',
                                          'https://www.metal-archives.com/bands/A_Forest_of_Stars/115504',
                                          'https://www.metal-archives.com/bands/Burzum/88',
                                          'https://www.metal-archives.com/bands/Mayhem/67',
                                          'https://www.metal-archives.com/bands/Satanic_Warmaster/989'])
        self.assertEqual(len(bands), 7)

if __name__ == '__main__':
    run_test_cases()
