# Write a Python function named triplets that takes a target number as input
# and returns a Pythagorean triplet (a, b, c) where a, b, and c are positive integers
# and a^2 + b^2 = c^2, such that the sum of a, b, and c equals the target number.
# If no such triplet exists, return None. Provide the function along with an example of its usage."
def triplets(target_num):
    # Iterate through possible values for 'x'
    for x in range(1, target_num):
        # Iterate through values greater than or equal to 'x' for 'y'
        for y in range(x, target_num):
            # Calculate 'z' such that the sum of 'x', 'y', and 'z' equals 'target_num'
            z = target_num - x - y
            # Check if (x, y, z) form a Pythagorean triplet
            if x ** 2 + y ** 2 == z ** 2:
                # If the condition is met, return the triplet
                return x, y, z
    # If no triplet is found, return None
    return None


# Call the function with target number 1000 and print the result
print(triplets(1000))
