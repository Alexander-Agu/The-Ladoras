import unittest
from unittest.mock import patch, MagicMock
from main import hotel_booking_system  

class TestHotelBookingSystem(unittest.TestCase):

    @patch('builtins.input', side_effect=['yes', 'Nokwanda', 'Xaba', 'nokwandaxaba487@gmail.com', '25', 'female', '2023-10-01 to 2023-10-05', 'Deluxe', '2', '200', 'yes'])
    @patch('send_email.send_email')
    @patch('sign_up.save_user_details')
    @patch('sign_up.find_user_details')
    @patch('booking.book_room', return_value=('2023-10-01 to 2023-10-05', 'Deluxe', 2, 200))
    def test_first_time_visitor(self, mock_book_room, mock_find_user_details, mock_save_user_details, mock_send_email, mock_input):
        hotel_booking_system()
        mock_save_user_details.assert_called_once_with('Nokwanda', 'Xaba', 'nokwandaxaba487@gmail.com', 25, 'female')
        mock_send_email.assert_called_once()

    @patch('builtins.input', side_effect=['no', 'John', 'Doe'])
    @patch('send_email.send_email')
    @patch('sign_up.find_user_details', return_value={'Name': 'Nokwanda', 'Surname': 'Xaba', 'Email': 'nokwandaxaba487@gmail.com'})
    @patch('booking.book_room', return_value=('2023-10-01 to 2023-10-05', 'Deluxe', 2, 200))
    def test_returning_visitor(self, mock_book_room, mock_find_user_details, mock_send_email, mock_input):
        hotel_booking_system()
        mock_find_user_details.assert_called_once_with('John', 'Doe')
        mock_send_email.assert_called_once()

    @patch('builtins.input', side_effect=['yes', 'Nokwanda', 'Xaba', 'nokwandaxaba487@gmail.com', '17', 'female'])
    def test_underage_registration(self, mock_input):
        with self.assertRaises(SystemExit):  # 
            hotel_booking_system()

    @patch('builtins.input', side_effect=['maybe'])
    def test_invalid_input(self, mock_input):
        with self.assertRaises(SystemExit): 
            hotel_booking_system()

if __name__ == '__main__':
    unittest.main()
