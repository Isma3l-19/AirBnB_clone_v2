import unittest
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place

class TestCreate(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def test_create_state_with_name(self):
        state_count = len(storage.all(State))
        self.cli.onecmd('create State name="California"')
        self.assertEqual(len(storage.all(State)), state_count + 1)
        self.cli.onecmd('create State name="Arizona"')
        self.assertEqual(len(storage.all(State)), state_count + 2)

    def test_create_place_with_params(self):
        place_count = len(storage.all(Place))
        self.cli.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        self.assertEqual(len(storage.all(Place)), place_count + 1)

if __name__ == "__main__":
    unittest.main()
