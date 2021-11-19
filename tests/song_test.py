import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Dreams", "Fleetwood Mac", 257)

    def test_has_name(self):
        self.assertEqual("Dreams", self.song.name)

    def test_has_artist(self):
        self.assertEqual("Fleetwood Mac", self.song.artist)

    def test_has_length(self):
        self.assertEqual(257, self.song.length)