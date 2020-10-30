import unittest
from city_functions import city_function

class citiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_string=city_function('santiago','chile')
        self.assertEqual(formatted_string,'Santiago,Chile')

    def test_city_country_population(self):
        formatted_string=city_function('santiago','chile','population=50000')
        self.assertEqual('Santiago,Chile - population=50000')

unittest.main()