import unittest
from src.roomtab import RoomTab
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoomTab(unittest.TestCase):
    
    def setUp(self):
        # self.room = Room(1, 2)
        # song = Song("Dreams", "Fleetwood Mac", 257)
        # self.guest_1 = Guest("Bob", 20.00, song)
        # self.guest_2 = Guest("Sally", 50.00, song)
        self.room_tab = RoomTab(1, 2)

    def test_has_room(self):
        expected = 1
        actual = self.room_tab.room_num
        self.assertEqual(expected, actual)

    def test_bill_initialised_to_0(self):
        expected = 0
        actual = len(self.room_tab.bill)
        self.assertEqual(expected, actual)

    def test_total_entry_fees__2_guests(self):
        expected = 10.00
        actual = self.room_tab.total_entry_fees()
        self.assertEqual(expected, actual)
  
    def test_add_drink_cost_to_bill(self):
        self.room_tab.add_drink_cost_to_bill(2.50)
        expected = 1
        actual = len(self.room_tab.bill)
        self.assertEqual(expected, actual)

    def test_total_drinks_bill__2_drinks(self):
        self.room_tab.add_drink_cost_to_bill(2.50)
        self.room_tab.add_drink_cost_to_bill(2.50)
        expected  = 5.00
        actual = self.room_tab.total_drinks_bill()
        self.assertEqual(expected, actual)
    
    def test_calculate_bill__2_guests_2_drinks(self):
        self.room_tab.add_drink_cost_to_bill(2.50)
        self.room_tab.add_drink_cost_to_bill(2.50)
        expected = 15.00
        actual = self.room_tab.calculate_bill()
        self.assertEqual(expected, actual)



    
    