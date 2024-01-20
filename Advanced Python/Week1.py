# a : Write a Python program to check if a number is a perfect square
# Time complexity : o(sqrt(n))
# Space complexity : o(1)
def check_perfect_square(number):
    # if the number is 0 or 1 it is square root, return true
    if number == 0 or number == 1:
        return True
    square_root_candidate = 2
    while square_root_candidate * square_root_candidate <= number:
        if (square_root_candidate * square_root_candidate) == number:
            return True
        square_root_candidate += 1
    return False


print("Checking if a number is perfect ", check_perfect_square(16))


# B- Write a Python program to find a missing number from a list.
# Time Complexity : o(n)
# Space Complexity : o(1)
def find_missing_number(numbers):
    # assuming the list is in ascending order and only one value other than the largest element is missing
    last_number = numbers[-1]
    # get sum of n numbers by using arithmetic  sum formula
    arithmetic_sum = last_number * (last_number + 1) / 2
    list_sum = sum(numbers)
    # subtracting given list sum from arithmetic sum gives the missing number
    return int(arithmetic_sum - list_sum)

print("Checking the missing number ", find_missing_number([1,2,4]))


# C- Write a Python program to find the single number in a list that doesn't occur twice.
# Time Complexity : o(n*k) where n is length of num_list and k is length of new_list
# Space Complexity : o(n)
def find_non_repated_number(num_list):
    new_list = []
    for num in num_list:
        if (num in new_list):
            new_list.remove(num)
        else:
            new_list.append(num)
    return new_list[0] if len(new_list) == 1 else -1


print(find_non_repated_number([1, 3, 2, 1, 2, 3, 4, 4]))
