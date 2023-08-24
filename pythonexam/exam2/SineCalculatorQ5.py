import math

def calculate_sin(x, n):
    output = 0.0
    sign = 1
    for i in range(1, n + 1, 2):
        term = (x ** i) / math.factorial(i)
        output += sign * term
        sign *= -1
    return output

x = float(input("Enter the value of x in degrees: "))
num = int(input("Enter a positive integer n: "))

# Convert user input to radians
radians_value = math.radians(x)

sin_x = calculate_sin(radians_value, num)

print(f"The sine of {x} degrees is : {sin_x:.5f}")
