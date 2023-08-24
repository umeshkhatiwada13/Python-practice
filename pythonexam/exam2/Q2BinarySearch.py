def binary_search(number_array, target_number):
    left, right = 0, len(number_array) - 1
    success = False

    while left <= right:
        mid = (left + right) // 2

        if number_array[mid] == target_number:
            success = True
            return [success, mid]
        elif number_array[mid] < target_number:
            left = mid + 1
        else:
            right = mid - 1

    return [success, None]


number_of_input = int(input("Enter the numbers of element in array : "))
input_list = []
i = 0
for a in range(0, number_of_input):
    num = int(input("Enter the number : "))
    input_list.append(num)
    i += 1
target_number = int(input("Enter the number to find : "))
data_list = binary_search(input_list, target_number)
success = data_list[0]
if success:
    print(f"The desired integer {target_number} is present in the list {input_list} at index {data_list[1]}.")
else:
    print(f"The desired integer {target_number} is not present in the list.")
