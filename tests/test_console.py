import unittest
from console import HBNBCommand
from models import *


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the test environment"""
        del self.console
        storage._FileStorage__objects = {}

    def test_create_with_params(self):
        """Test creating objects with parameters"""
        self.console.onecmd("create State name='California'")
        self.assertEqual(len(storage.all()), 1)
        self.assertIsInstance(list(storage.all().values())[0], State)
        self.assertEqual(list(storage.all().values())[0].name, 'California')
        self.console.onecmd("create Place city_id='0001' user_id='0001'
                            name='My_little_house'
                            number_rooms=4 number_bathrooms=2
                            max_guest=10 price_by_night=300")
        self.assertEqual(len(storage.all()), 2)
        self.assertIsInstance(list(storage.all().values())[1], Place)
        place = list(storage.all().values())[1]
        self.assertEqual(place.city_id, '0001')
        self.assertEqual(place.user_id, '0001')
        self.assertEqual(place.name, 'My little house')
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)


if __name__ == '__main__':
    unittest.main()
