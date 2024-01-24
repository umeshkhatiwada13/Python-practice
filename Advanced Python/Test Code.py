# Space Complexity: O(n) - Dominated by the complement_set, which stores unique complements.
# In the worst case, the set could store approximately n/2 unique values.
# Time Complexity: O(n^2) - Two nested loops, iterating through combinations of elements in the array.
def find_three_numbers(arr):
    """
    Find triplets in the array whose sum is zero.

    :param arr: Input array
    :return: List of triplets whose sum is zero
    """
    result = []  # List to store the triplets whose sum is zero
    complement_set = set()  # Set to store unique complements

    # Iterate through the array up to the third-to-last element
    # Time Complexity: O(n^2) - Two nested loops
    for i in range(len(arr) - 2):
        # Nested loop to iterate through elements after arr[i]
        for j in range(i + 1, len(arr) - 1):
            complement = -arr[i] - arr[j]  # Calculate the complement needed for a triplet
            if complement in complement_set:
                result.append([complement, arr[i], arr[j]])  # Found a triplet, add it to the result
            complement_set.add(arr[j])  # Add arr[j] to the set to store complements for future elements

    return result

arr = [-1, 0, 1, 2, -1, -4]
result = find_three_numbers(arr)
print(result)

