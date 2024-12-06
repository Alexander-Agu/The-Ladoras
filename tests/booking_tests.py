import unittest
from unittest.mock import patch
from rooms import room_availability, type_package
from booking import book_room

class TestBookRoom(unittest.TestCase):

    def setUp(self):
        # Backup and restore the global state of room_availability before each test
        self.original_room_availability = room_availability.copy()

    def tearDown(self):
        # Restore the original room availability after each test
        global room_availability
        room_availability = self.original_room_availability

    @patch("builtins.input", side_effect=["5", "10", "common"])
    def test_successful_booking_common(self, mock_input):
        selected_dates, room_choice, nights, total_price = book_room()
        self.assertEqual(selected_dates, "2024-12-05 to 2024-12-10")
        self.assertEqual(room_choice, "common")
        self.assertEqual(nights, 5)
        self.assertEqual(total_price, 7500)  # 1500 * 5
        self.assertEqual(room_availability["common"], self.original_room_availability["common"] - 1)

    @patch("builtins.input", side_effect=["15", "20", "precidential"])
    def test_successful_booking_precidential(self, mock_input):
        selected_dates, room_choice, nights, total_price = book_room()
        self.assertEqual(selected_dates, "2024-12-15 to 2024-12-20")
        self.assertEqual(room_choice, "precidential")
        self.assertEqual(nights, 5)
        self.assertEqual(total_price, 25000)  
        self.assertEqual(room_availability["precidential"], self.original_room_availability["precidential"] - 1)

    @patch("builtins.input", side_effect=["31", "1", "common"])
    def test_invalid_date_range(self, mock_input):
        with self.assertRaises(StopIteration):  
            book_room()

    @patch("builtins.input", side_effect=["10", "15", "luxury"])
    def test_invalid_room_type(self, mock_input):
        with self.assertRaises(StopIteration):  
            book_room()

    @patch("builtins.input", side_effect=["10", "15", "standard", "standard"])
    def test_fully_booked_room(self, mock_input):
        global room_availability
        room_availability["standard"] = 0  
        with self.assertRaises(StopIteration): 
            book_room()

if __name__ == "__main__":
    unittest.main()
