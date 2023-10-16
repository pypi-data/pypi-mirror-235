
import os
import unittest

from datetime import datetime
from configparser import ConfigParser

import pandas as pd

from .util import Submodule, prepare_submodule


class TestAlbums(unittest.TestCase):
    def test_album_profile(self):
        
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Album', dir(export))

        album = export.Album.get_profile('https://www.metal-archives.com/albums/Urfaust/Untergang/1161736')
        self.assertIsNotNone(album)

    def test_album_profiles(self):
        
        export = prepare_submodule(Submodule.EXPORT)
        self.assertIsNotNone(export)

        self.assertIn('Album', dir(export))

        album = export.Album.get_profiles(['https://www.metal-archives.com/albums/Urfaust/Untergang/1161736',
                                           'https://www.metal-archives.com/albums/Furia/Huta_Luna/1166382',
                                           'https://www.metal-archives.com/albums/Hades_Almighty/...Again_Shall_Be/91367'])
        self.assertIsNotNone(album)
