import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Dreams", "Fleetwood Mac", 257)
        self.guest = Guest("Bob", 20.00, self.song)
        self.room = Room(1, 1)

    def test_has_name(self):
        self.assertEqual("Bob", self.guest.name)

    def test_has_cash(self):
        self.assertEqual(20.00, self.guest.cash)

    def test_reduce_cash__sufficient_funds(self):
        self.guest.reduce_cash(5.00)
        expected = 15.00
        actual = self.guest.cash
        self.assertEqual(expected, actual)

    def test_reduce_cash__insufficient_funds(self):
        self.guest.reduce_cash(21.00)
        expected = 20.00
        actual = self.guest.cash
        self.assertEqual(expected, actual)

    def test_has_favourite_song(self):
        expected = "Dreams"
        actual = self.guest.fav_song.title
        self.assertEqual(expected, actual)

    def test_check_fav_song__room_has_song(self):
        self.room.add_song(self.song)
        expected = "Whoo!"
        actual = self.guest.check_for_fav_song(self.room)
        self.assertEqual(expected, actual)

    def test_check_fav_song__room_does_not_have_song(self):
        song_2 = Song("Changes", "Tupac", 268)
        self.room.add_song(song_2)
        expected = None
        actual = self.guest.check_for_fav_song(self.room)
        self.assertEqual(expected, actual)
       