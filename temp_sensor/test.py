import unittest

from functions import *


class TemperatureSensorTests(unittest.TestCase):
    def test_conversion(self):
        """
        Test that it can convert from C to F
        """
        data = 100
        result = cToF(data)
        self.assertEqual(result, 212)

    def test_background_cold(self):
        """
        Test the background is blue when cold
        """

        data = 32
        result = setBackgroundColor(data)
        self.assertEqual(result, { "red": 0, "green": 128, "blue": 64 })
    def test_background_warm(self):
        """
        Test the background is green when warm
        """

        data = 70
        result = setBackgroundColor(data)
        self.assertEqual(result, { "red": 0, "green": 255, "blue": 0 })

    def test_background_hot(self):
        """
        Test the background is red when hot
        """

        data = 90
        result = setBackgroundColor(data)
        self.assertEqual(result, { "red": 255, "green": 0, "blue": 0 })


if __name__ == '__main__':
    unittest.main()
