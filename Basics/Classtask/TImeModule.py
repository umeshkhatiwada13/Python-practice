import datetime

# current_datetime = datetime.datetime.now()
# print(current_datetime)
# print("Year ", current_datetime.year)
# print("Month ", current_datetime.month)
# print("Day ", current_datetime.day)

import datetime

# Get the user input for the birthday
birthday = input("Enter your birthday (yyyy-MM-dd): ")

# Convert the user input to a datetime object
birthdate = datetime.datetime.strptime(birthday, "%Y-%m-%d")

# Calculate the time difference between birthdate and epoch (1970-01-01)
time_difference = datetime.datetime.now() - birthdate

# Calculate the total number of seconds
total_seconds = int(time_difference.total_seconds())

# Display the total number of seconds lived in epoch time
print("Total seconds lived in epoch time:", total_seconds)
