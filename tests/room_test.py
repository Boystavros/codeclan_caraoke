import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.roomtab import RoomTab


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 1)
        self.song_1 = Song("Dreams", "Fleetwood Mac", 257)       
        self.guest_1 = Guest("Bob", 20.00, self.song_1)
        self.guest_2 = Guest("Sally", 50.00, self.song_1)
        self.room_tab = RoomTab(self.room.number)

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

    # No longer required after max_guests property added with suitable tets
    # def test_check_in(self):
    #     self.room.check_in(self.guest_1)
    #     result = len(self.room.guests)
    #     self.assertEqual(1, result)

    def test_check_out__guest_in_room(self):
        self.room.check_in(self.guest_1)
        self.room.check_out(self.guest_1)
        result = len(self.room.guests)
        self.assertEqual(0, result)

    def test_check_out__guest_not_in_room(self):
        self.room.check_in(self.guest_1)
        self.room.check_out(self.guest_2)
        result = len(self.room.guests)
        self.assertEqual(1, result)
            
    def test_add_song(self):
        self.room.add_song(self.song_1)
        result = len(self.room.songs)
        self.assertEqual(1, result)
    
    def test_remove_song__song_in_songs(self):
        self.room.add_song(self.song_1)
        self.room.remove_song(self.song_1)
        result = len(self.room.songs)
        self.assertEqual(0, result)

    def test_remove_song__song_not_in_songs(self):
        song_2 = Song("Changes", "Tupac", 268)        
        self.room.add_song(self.song_1)
        self.room.remove_song(song_2)
        result = len(self.room.songs)
        self.assertEqual(1, result)

    def test_has_max_guests(self):
        expected = 1
        actual = self.room.max_guests
        self.assertEqual(expected, actual)

    def test_check_in__room_has_capacity(self):
        expected = "Guest Bob added to room 1."
        actual = self.room.check_in(self.guest_1)
        self.assertEqual(expected, actual)

    def test_check_in__room_is_full(self):
        self.room.check_in(self.guest_1)
        expected = "Room 1 is full, cannot add Sally to room."
        actual = self.room.check_in(self.guest_2)
        self.assertEqual(expected, actual)
        
    # No longer required as RoomTab now has entry fee data
    # def test_has_entry_fee(self):
    #     expected = 5.00
    #     actual = self.room.entry_fee
    #     self.assertEqual(expected, actual)

    def test_has_room_tab__room_1(self):
        expected = 1
        actual = self.room.room_tab.room_num
        self.assertEqual(expected, actual)
             
    def test_check_in_adds_guest_to_room_tab(self):
        self.room.check_in(self.guest_1)
        expected = 1
        actual = self.room.room_tab.guests
        self.assertEqual(expected, actual)

    def test_sell_drink__cost_2(self):
        self.room.sell_drink(2.00)
        expected = 2.00
        actual  = self.room.room_tab.total_drinks_bill()
        self.assertEqual(expected, actual)

    def test_retrieve_bill__1_guest_1_drink(self):
        self.room.check_in(self.guest_1)
        self.room.sell_drink(2.50)
        expected = 7.50
        actual = self.room.retrieve_bill()
        self.assertEqual(expected, actual)
    
    def test_charge_guest__guest_1_5_of_10(self):
        self.room.check_in(self.guest_1)
        self.room.sell_drink(2.50)
        self.room.sell_drink(2.50)
        self.room.charge_guest(self.guest_1, 5.00)
        expected_bill = 5.00
        actual_bill = self.room.retrieve_bill()
        expected_guest_cash = 15.00
        actual_guest_cash = self.guest_1.cash
        self.assertEqual(expected_bill, actual_bill)
        self.assertEqual(expected_guest_cash, actual_guest_cash)