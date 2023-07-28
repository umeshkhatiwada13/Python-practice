import datetime

# current date and time
now = datetime.datetime.now()

# take user input
birthday = input("Enter your birthday (Accepted Format YYYY-MM-DD): ")

# Convert the user input to a datetime object
birthdate = datetime.datetime.strptime(birthday, "%Y-%m-%d")

# calculate time difference till today from user birthday
time_difference = now - birthdate

# Calculate the current age
current_age = int(time_difference.days / 365)

# Calculate the next birthday
next_birthday = birthdate.replace(year=now.year)

if next_birthday < now:
    next_birthday = next_birthday.replace(year=now.year + 1)

# Calculate the time difference until the next birthday
time_until_next_birthday = next_birthday - now

# Convert time difference to days, hours, minutes, and seconds
total_seconds = time_until_next_birthday.total_seconds()
days = int(total_seconds // (24 * 3600))
total_seconds %= 24 * 3600
hours = int(total_seconds // 3600)
total_seconds %= 3600
minutes = int(total_seconds // 60)
seconds = int(total_seconds % 60)

# Display the current age
print("Your Current age:", current_age)
# display time until user's next birthday
print("Tour next birthday is in {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
