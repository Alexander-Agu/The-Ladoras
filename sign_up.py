import csv
import os

# Function to save user details to a CSV file
def save_user_details(name, surname, email, age, gender):
    file_exists = os.path.isfile("users.csv")
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Surname", "Email", "Age", "Gender"])
        writer.writerow([name, surname, email, age, gender])

# Function to check if a returning user's details exist
def find_user_details(name, surname):
    if not os.path.isfile("users.csv"):
        return None
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower() and row["Surname"].lower() == surname.lower():
                return row
    return None