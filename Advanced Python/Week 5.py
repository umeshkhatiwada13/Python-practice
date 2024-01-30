# Write a Python program to find all the numbers from 0-9 from a string:
# input: '89ADFRE41'
# Output :[8941]

def get_numbers(input_string):
    print(input_string)
    number = ''
    for x in input_string:
        if (x.isnumeric()):
            number += x
    return number


print(get_numbers('123adk'))


# Write a Python program to find two elements once in a list where every element appears exactly n times in the list.
# Input : [1, 2, 1, 3, 2, 5], 2    (n=2)
# Output :[5, 3]

def get_n_repeated(input_array, repetition):
    number_tracker = {}
    for x in input_array:
        number_tracker[x] = number_tracker.get(x, 0) + 1

    result = []
    for k, v in number_tracker.items():
        if (repetition == v):
            result.append(k)
    return result


print(get_n_repeated([1, 2, 2, 3, 4, 5, 3, 5, 3], 1))


# Write a Python program to reverse the digits of an integer.
# Input : 234
# Input : -234
# Output: 432
# Output : -432

def reverse_integer(number):
    is_negative = number < 0
    if (is_negative): number * -1
    reverse_num = ''
    while (number > 0):
        reverse_num = reverse_num +  str(number % 10)
        number = int(number / 10)

    return int(reverse_num) * -1 if is_negative else reverse_num

print(reverse_integer(-123))
