import unittest
import os
import csv
import tempfile
from sign_up import save_user_details, find_user_details  

class TestUserDetailsFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()
        self.csv_path = self.test_file.name
        self.original_file = "users.csv"

        # Redirect the actual file to the temporary file
        if os.path.exists(self.original_file):
            os.rename(self.original_file, self.original_file + ".backup")
        os.rename(self.csv_path, self.original_file)

    def tearDown(self):
        # Clean up by removing the test file and restoring the original file
        os.remove(self.original_file)
        if os.path.exists(self.original_file + ".backup"):
            os.rename(self.original_file + ".backup", self.original_file)

    def test_save_user_details_creates_file(self):
        save_user_details("nokwanda", "xaba", "nokwandaxaba487@gmail.com", 25, "Female")
        self.assertTrue(os.path.exists(self.original_file))

    def test_save_user_details_writes_correct_data(self):
        save_user_details("kolobe","mabotha","ksmabotha@gmail.com",76,"Male")
        with open(self.original_file, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Name"], "kolobe")
        self.assertEqual(rows[0]["Surname"], "mabotha")
        self.assertEqual(rows[0]["Email"], "ksmabotha@gmail.com")
        self.assertEqual(rows[0]["Age"], "76")
        self.assertEqual(rows[0]["Gender"], "Male")

    def test_find_user_details_existing_user(self):
        save_user_details("alex","agu","theonlyagu@gmail.com",21,"Male")
        user = find_user_details("alex","agu")
        self.assertIsNotNone(user)
        self.assertEqual(user["Email"], "theonlyagu@gmail.com")
        self.assertEqual(user["Age"], "21")

    def test_find_user_details_nonexistent_user(self):
        save_user_details("Bob", "Marley", "bob.marley@example.com", 35, "Male")
        user = find_user_details("Charlie", "Brown")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
