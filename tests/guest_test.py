import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Bob", 20.00)

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