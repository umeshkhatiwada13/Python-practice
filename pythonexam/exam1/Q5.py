num = 0  # The starting number of organisms
avg = 0.0  # The average daily increase
days = 0  # The number of days to multiply

# Get a valid value for the starting number of
# organisms from the user.
num = int(input("Enter the number of Organisms : "))
avg = float(input("Average daily increase: "))
days = int(input("Number of days to multiply: "))

print('-----------------------------------')
print("Input given by User ")
print("Average daily increase ", num)
print("Number of days to multiply: ", num)

# Determine if the average daily increase was
# input as a whole number; if so, divide by
# 100 to format the value as a percentage.
if avg >= 1.0:
    avg /= 100.0

# Calculate and print amount of increase each day.
print('Day Approximate\t\t Population')
print('-----------------------------------')

for day in range(days):
    # Apply the increase after the first day.
    if day > 0:
        num += (num * avg)
    print((day + 1), '\t\t\t\t\t\t', num)
