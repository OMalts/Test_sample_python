import unittest
from main import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi*1**2)
        self.assertEqual(circle_area(0), pi*0**2)
        self.assertEqual(circle_area(2.506), pi*2.506**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area(-2))
        self.assertRaises(ValueError, circle_area(-1))