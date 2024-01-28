# Write a Python program to find the single element in a list where every element appears multiple times except for one.
# Input : [5, 3, 4, 3, 5, 5, 3],
# Output : 4
def find_non_repeating(number_list):
    number_tracker = {}  # number_tracker<number,number_count>
    for x in number_list:
        #       get the count of x, 0 if not present ,add 1 to the original count and push back to dictionary
        number_tracker[x] = number_tracker.get(x, 0) + 1

    single_element = -1
    for key, value in number_tracker.items():
        if value == 1:
            single_element = key
    return single_element


print(find_non_repeating([5, 3, 4, 4, 3, 5, 5, 3]))


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
    root = -1
    while init_number * init_number <= number:
        if init_number * init_number == number:
            root = init_number
        init_number = init_number + 1
    return root


print("Square root of number is ", get_square_root(2253))

# Write a Python program to check a sequence of numbers is a geometric progression or not.
# Input : [2, 6, 18, 54]
# Output : True

import math


def check_gp(num_array):
    length = len(num_array)
    if length < 2 | any(element == 0 for element in num_array):
        return False
    # get ratio for GM
    r = num_array[1] / num_array[0] if num_array[0] != 0 else 0
    # initial supposition : The array's value are in GM
    is_gp = True
    for counter, value in enumerate(num_array[1:]):
        # if the next number doesnot equals GP calculate by the formula with previous number , the sequence is not in GM
        if (value != num_array[counter] * r):
            is_gp = False
            break
    return is_gp


print(check_gp([2, 6, 18, 54, 162]))
# for x in num_array:


# Test cases for checkgp function
test_cases = [
    # Geometric Progression: 2, 6, 18, 54, 162 (Common ratio: 3)
    ([2, 6, 18, 54, 162], True),
    # Geometric Progression: 1, 5, 25, 125, 625 (Common ratio: 5)
    ([1, 5, 25, 125, 625], True),
    # Geometric Progression: 3, 9, 27, 81, 243 (Common ratio: 3)
    ([3, 9, 27, 81, 243], True),
    # Not a Geometric Progression: Random sequence
    ([1, 2, 3, 4, 5], False),
    # Not a Geometric Progression: Empty list
    ([], False),
    # Not a Geometric Progression: Single element
    ([100], False),
    # Not a Geometric Progression: Single element (0)
    ([0], False),
    # Not a Geometric Progression: All elements are 0
    ([0, 0, 0, 0], False),
]


# Function to test checkgp function
def run_tests(check_gp):
    for i, (sequence, expected_result) in enumerate(test_cases):
        result = check_gp(sequence)
        print(f"Test case {i + 1}: {'PASS' if result == expected_result else 'FAIL'}")

run_tests(check_gp)
