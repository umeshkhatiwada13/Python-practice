# Variables to represent the base hours and
# the overtime multiplier.
Base_hours = 40  # Base hours per week
ot_multiplier = 1.5  # Overtime multiplier

# Get the hours worked and the hourly pay rate from users.
hours = int(input("Enter the hours worked : "))
pay_rate = int(input("Enter the payrate : "))

# declare overtime pay and hours 0 initially
overtime_pay = 0
overtime_hours = 0
initial_pay = 0
# Calculate and display the gross pay.
if hours > Base_hours:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked
    # Calculate the amount of overtime pay.
    overtime_hours = hours - Base_hours
    overtime_pay = overtime_hours * pay_rate * ot_multiplier
    # Calculate the gross pay.
    initial_pay = Base_hours * pay_rate
    # add overtime pay to gross pay
    gross_pay = initial_pay + overtime_pay
else:
    gross_pay = hours * pay_rate

# Display the gross pay.
print("Overtime hours :", overtime_hours)
print("Overtime pay :", overtime_pay)
if hours > Base_hours:
    print("Gross Pay without overtime : ", initial_pay)
else:
    print("Gross Pay without overtime : ", gross_pay)
print("Gross Pay with overtime : ", gross_pay)
