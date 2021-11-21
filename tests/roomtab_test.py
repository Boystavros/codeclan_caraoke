import unittest
from src.roomtab import RoomTab

class TestRoomTab(unittest.TestCase):
    
    def setUp(self):
        self.room_tab = RoomTab(1)

    def test_has_room_num(self):
        expected = 1
        actual = self.room_tab.room_num
        self.assertEqual(expected, actual)


    def test_bill_initialised_to_0(self):
        expected = 0
        actual = len(self.room_tab.bill)
        self.assertEqual(expected, actual)

    def test_total_entry_fees__0_guests(self):
        expected = 0.00
        actual = self.room_tab.total_entry_fees()
        self.assertEqual(expected, actual)

    def test_increase_guests_on_tab(self):
        self.room_tab.increase_guests_on_tab()
        expected = 1
        actual = self.room_tab.guests
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
        self.room_tab.increase_guests_on_tab()
        self.room_tab.increase_guests_on_tab()
        self.room_tab.add_drink_cost_to_bill(2.50)
        self.room_tab.add_drink_cost_to_bill(2.50)
        expected = 15.00
        actual = self.room_tab.calculate_bill()
        self.assertEqual(expected, actual)

    def test_reduce_bill__5_from_10(self):
        self.room_tab.increase_guests_on_tab()
        self.room_tab.increase_guests_on_tab()
        self.room_tab.add_drink_cost_to_bill(2.50)
        self.room_tab.add_drink_cost_to_bill(2.50)
        self.room_tab.reduce_bill(5.00)
        expected = 10.00
        actual = self.room_tab.calculate_bill()
        self.assertEqual(expected, actual)

    
    