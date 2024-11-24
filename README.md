# The-Ladoras
A terminal based Hotel Booking System

# Functionalities
* Check how many rooms are available
* Rooms should be in different packages ( Presidential, Common, Intermediate )
* User's should be able to book a room
* User's should not be able to book a room thats already been booked
* Prices vary depensing on the type of package and how many nights the user chooses to spend at the hotel
* Using the `Google calender API` user's must be sent an email confirming their BOOKING

# Hotel rooms should vary by packages
The higher the rate of the package the more expensive rooms in that catagory are
Common -> 1Star
Intermidiate -> 2Star
Precidential -> 3Star

# Properties of a room
1. Type of package
2. Room number
3. Checked if its booked or not
4. Number of nights to be spent in that room
4. Date showing start and end date of the duration of the booking / If not booked it should be empty
* Package = { "Room Number(1st)": { "Booked": True, "Nights": 2, "Date": 01/11/24 - 02/11/34 } }