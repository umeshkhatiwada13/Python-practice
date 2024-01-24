# 2-Write a Python program to find the single element appears once in a list where every element appears multiple times except for one.
# Input : [1, 1, 1, 2, 2, 2, 3]

def print_non_repeating_number(number_list):
    tracker = {}
    single_number = 0
    for number in number_list:
        if number not in tracker:
            tracker[number] = False
        else:
            tracker[number] = True

    for k, v in tracker.items():
        if not v:
            single_number = k
    return single_number


print("Non repeating numbers:", print_non_repeating_number([1, 1, 1, 1, 2, 2, 2, 4]))


# 3-Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
# Input : 48
# Output : 3
# For example given number is 59, the result will be 5.
def print_single_digit(number):
    while number > 9:
        number = int(number / 10) + number % 10
    return number

print("Single digit number ", print_single_digit(346))


