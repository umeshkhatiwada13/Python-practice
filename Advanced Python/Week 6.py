# 1-Write a Python program to check a sequence of numbers is an arithmetic progression or not.
# Input : [5, 7, 9, 11]
# Output : True
# In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
# For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
def check_ap(number_array):
    array_length = len(number_array)
    if array_length < 2:
        return False

    is_ap = True
    diff = number_array[1] - number_array[0]
    counter = 2
    for value in number_array[2:]:
        if number_array[counter] - number_array[counter - 1] != diff:
            is_ap = False
            break
    return is_ap


print(check_ap([5, 7, 9, 11]))


# 2-Write a Python program to check whether a given number is an ugly number.
# Input : 12
# Output : True
# Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
# shows the first 10 ugly numbers.
# Note: 1 is typically treated as an ugly number


# 3-Write a Python Function to find the single number in a list that doesn't occur n times.
# Input : [5, 3,3,4, 4, 3, 4], N=3
# Output : 5
def get_non_repeating_number(number_array, n):
    word_count_dictionary = {}
    for x in number_array:
        word_count_dictionary[x] = word_count_dictionary.get(x, 0) + 1
    print(word_count_dictionary)

    final_item = -1
    for k, v in word_count_dictionary.items():
        if v != n:
            final_item = k
            break
    return final_item


print(get_non_repeating_number([5, 3, 3, 4, 4, 3, 4],3))
