
import unittest

from cities import city_country

class TestCityCountry(unittest.TestCase):
    """ Tests the function city_country()"""

    def test_city_country_1(self):
        neat_name = city_country("Lahore", "Pakistan")
        self.assertEqual(neat_name, "Lahore, Pakistan")

unittest.main()