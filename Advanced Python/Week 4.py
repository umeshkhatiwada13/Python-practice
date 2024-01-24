# Write a Python program to find the single element in a list where every element appears multiple times except for one.
# Input : [5, 3, 4, 3, 5, 5, 3],
# Output : 4

def find_non_repeating(number_list):
    number_tracker = {}
    for x in number_list:
        number_tracker.get(x, 0)


# Write a Python program to compute and return the square root of a given 'integer'.
# Input : 16
# Output : 4
# Note : The returned value will be an 'integer', do not use square root functions from python.

def get_square_root(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    init_number = 2
    tracker = 2
    while init_number * init_number <= number:
        if (init_number * init_number == number):
            tracker = init_number
        init_number = tracker + 1
    return init_number


print("Square root of number is ", get_square_root(16))
