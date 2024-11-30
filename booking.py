import calendar
from rooms import room_availability
from rooms import type_package

# Function to handle booking process
def book_room():
    print("Let's proceed with your booking. \n")

    # Display available dates
    year = 2024
    month = 12
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatmonth(year, month)) # Prints the calenders format

    # Date range selection
    while True:
        try:
            check_in_date = int(input("Enter your check-in date (1-31): "))
            check_out_date = int(input("Enter your check-out date (1-31): "))
            if (1 <= check_in_date <= calendar.monthrange(year, month)[1] and
                    1 <= check_out_date <= calendar.monthrange(year, month)[1] and
                    check_in_date < check_out_date):
                
                selected_dates = f"{year}-{month:02d}-{check_in_date:02d} to {year}-{month:02d}-{check_out_date:02d}"
                print(f"Your stay is from {selected_dates}.\n")
                break
            else:
                print("Invalid date range. Please try again.")
        except ValueError:
            print("Please enter valid numbers.")

    # Display room options
    print("We have the following rooms available:")
    type_count = 0
    for room, count in room_availability.items():
        print(" ")
        print(f"- {room.capitalize()} (Available: {count})\n")
        print(f"Type:\n{type_package[type_count]}")
        print("__________________________________________________")
        type_count += 1

    # Checks if the
    while True:
        room_choice = input("Enter the type of package you want to book ( * common * / ** standard ** / *** precidential ***): ").strip().lower()
        if room_choice in room_availability and room_availability[room_choice] > 0:
            room_availability[room_choice] -= 1
            print(f"\nYou have booked the {room_choice} package. Remaining {room_choice} rooms: {room_availability[room_choice]}")
            break
        elif room_choice in room_availability:
            print(f"\nSorry, no {room_choice} rooms are available.")
        else:
            print("\nInvalid room type. Please select a valid option.")

    # Price calculation
    prices = {"common": 1500, "standard": 3000, "precidential": 5000}
    nights = check_out_date - check_in_date
    total_price = prices[room_choice] * nights
    print(f"The price for {room_choice} package is R{prices[room_choice]} per night.")
    print(f"For {nights} nights, the total price is R{total_price}.\n")
    return selected_dates, room_choice, nights, total_price