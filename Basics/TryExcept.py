
try:
    divident = int(input("Enter a number: "))
    divisor = int(input("Enter the number to divide by: "))
    result = divident /divisor
    print("Result is {}".format(result))
except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)

