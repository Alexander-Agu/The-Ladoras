import calendar
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import os

# Initialize room availability
room_availability = {
    "penthouse": 2,
    "executive": 3,
    "standard": 5,
}


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

# Function to handle booking process
def book_room():
    print("Let's proceed with your booking.")

    # Display available dates
    year = 2024
    month = 12
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatmonth(year, month))

    # Date range selection
    while True:
        try:
            check_in_date = int(input("Enter your check-in date (1-31): "))
            check_out_date = int(input("Enter your check-out date (1-31): "))
            if (1 <= check_in_date <= calendar.monthrange(year, month)[1] and
                    1 <= check_out_date <= calendar.monthrange(year, month)[1] and
                    check_in_date < check_out_date):
                selected_dates = f"{year}-{month:02d}-{check_in_date:02d} to {year}-{month:02d}-{check_out_date:02d}"
                print(f"Your stay is from {selected_dates}.")
                break
            else:
                print("Invalid date range. Please try again.")
        except ValueError:
            print("Please enter valid numbers.")

    # Display room options
    print("We have the following rooms available:")
    for room, count in room_availability.items():
        print(f"- {room.capitalize()} (Available: {count})")

    while True:
        room_choice = input("Enter the room type you want to book (penthouse/executive/standard): ").strip().lower()
        if room_choice in room_availability and room_availability[room_choice] > 0:
            room_availability[room_choice] -= 1
            print(f"You have booked a {room_choice}. Remaining {room_choice} rooms: {room_availability[room_choice]}")
            break
        elif room_choice in room_availability:
            print(f"Sorry, no {room_choice} rooms are available.")
        else:
            print("Invalid room type. Please select a valid option.")

    # Price calculation
    prices = {"penthouse": 500, "executive": 300, "standard": 150}
    nights = check_out_date - check_in_date
    total_price = prices[room_choice] * nights
    print(f"The price for {room_choice} is R{prices[room_choice]} per night.")
    print(f"For {nights} nights, the total price is R{total_price}.")
    return selected_dates, room_choice, nights, total_price


def hotel_booking_system():
    print("Welcome to Hotel X")

    
    question_1 = input("Are you a first-time visitor? (yes/no): ").strip().lower()

    if question_1 == "yes":
        print("We will now take you through the registration process.")

        name = input("Enter your first name: ").strip()
        surname = input("Enter your surname: ").strip()
        email = input("Enter your email address: ").strip()

        while True:
            try:
                age = int(input("Enter your age: "))
                if age >= 18:
                    break
                else:
                    print("You must be over 18 to make a booking.")
            except ValueError:
                print("Please enter a valid number.")

        gender = input("Are you male or female? ").strip().capitalize()
        save_user_details(name, surname, email, age, gender)
        print(f"Welcome to Hotel X, {name} {surname}! Your details have been saved for future reference.")

    else:
        name = input("Enter your first name: ").strip()
        surname = input("Enter your surname to confirm: ").strip()
        user_details = find_user_details(name, surname)
        if user_details:
            print(f"Welcome back, {user_details['Name']} {user_details['Surname']}!")
        else:
            print("We could not find your details. Please register again.")
            return

    selected_dates, room_choice, nights, total_price = book_room()

    confirm = input("Would you like to confirm your booking? (yes/no): ").strip().lower()
    if confirm == "yes":
        print(f"Thank you for booking with us! Your stay is confirmed from {selected_dates}.")
    else:
        print("Booking canceled.")

hotel_booking_system()