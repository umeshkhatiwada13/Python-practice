# Constants for the increase in tuition per year,
# and the starting tuition amount.
INCREASE_PER_YEAR = 0.23
STARTING_AMOUNT = 7000.0

# Declare a variable to store the tuition.
tuition = STARTING_AMOUNT

# Calculate and print amount of increase each year for atleast 7 years.
# Looping for 7 years , 8 is exclusive
for year in range(1, 8):
    # calculate the increased fee for the year
    increased_fee = tuition * INCREASE_PER_YEAR
    # Increase the tuition by INCREASE_PER_YEAR as specified above
    tuition += increased_fee
    print("Tuition for Year {0} is {1}".format(year, tuition))
    print("Increased fee {0}".format(increased_fee))
