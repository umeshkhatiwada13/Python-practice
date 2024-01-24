def get_max_sum(arr):
    left_pointer = 0
    right_pointer = len(arr)
    max_sum = 0
    while left_pointer < right_pointer:
        max_sum = arr[left_pointer] + arr[right_pointer] if arr[left_pointer] + arr[right_pointer]  > max_sum else max_sum
    return 0

get_max_sum({100,200,300})