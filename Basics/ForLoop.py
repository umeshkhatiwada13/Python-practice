fruitList = ["Apple", "Banana", "Cherry", "Mango", "Guava"]

for fruit in fruitList:
    print(fruit)

# Using range for printing number from 1 to 4(5 is exclusive)
for num in range(1, 5):
    print(num)

# Using range to print number with 3 increment in each loop(default is 1)
for num in range(1, 20, 3):
    print("Number {}".format(num))

for number in range(1, 10):
    if number % 2 == 0:
        print("This is even number")
    else:
        # Sometime in case we don't have any code to write inside for loop, we can write pass to avoid error
        # it don't actually do anything and is not same as continue as continue prevents execution
        # of code below that line
        pass
