import unittest
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1)
        self.guest = Guest("Bob", 20.00)

    def test_has_number(self):
        expected = 1
        actual = self.room.number
        self.assertEqual(expected, actual)

    def test_guests_initialised_empty(self):
        actual = len(self.room.guests)
        self.assertEqual(0, actual)

    def test_songs_initialised_empty(self):
        actual = len(self.room.songs)
        self.assertEqual(0, actual)

    def test_check_in(self):
        self.room.check_in(self.guest)
        actual = len(self.room.guests)
        self.assertEqual(1, actual)
