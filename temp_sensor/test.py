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

    def test_background_error(self):
        """
        Test the background in case of an error
        """

        data = float('nan')
        result = setBackgroundColor(data)
        self.assertEqual(result, { "red": 255, "green": 255, "blue": 0})

    def test_set_output(self):
        """
        Test the text if the temp and humidity are valid
        """

        temp = 32
        hum = 65
        result = setOutput(temp, hum)
        self.assertEqual(result, "Temp:" + str(temp) + "F\nHumidity: " + str(hum) + "%")

    def test_set_output_json(self):
        """
        Test the text if the temp and humidity are valid. Return JSON
        """

        temp = 32
        hum = 65
        ts = str(datetime.datetime.now())
        result = setOutput(temp, hum, "json", timestamp = ts)
        self.assertEqual(result, {'timestamp': ts, 'temperature': temp, 'humidity': hum})


if __name__ == '__main__':
    unittest.main()
