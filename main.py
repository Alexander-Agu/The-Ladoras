import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sign_up import save_user_details
from sign_up import find_user_details
from booking import book_room

def hotel_booking_system():
    print("Welcome to the Ladora Springs:\n")
    
    question_1 = input("Are you a first-time visitor? (yes/no): ").strip().lower()

    if question_1 in "yes":
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

    elif question_1 in "no":
        name = input("Enter your first name: ").strip()
        surname = input("Enter your surname to confirm: ").strip()
        user_details = find_user_details(name, surname)
        if user_details:
            print(f"Welcome back, {user_details['Name']} {user_details['Surname']}!")
        else:
            print("We could not find your details. Please register again.")
            return
    else:
        print("\nPlease give us an answer we can understand \nRegister with us again.")
        return

    selected_dates, room_choice, nights, total_price = book_room()

    confirm = input("Would you like to confirm your booking? (yes/no): ").strip().lower()
    if confirm in "yes":
        print(f"Thank you for booking with us! Your stay is confirmed from {selected_dates}.")
    else:
        print("Booking canceled.")

hotel_booking_system()