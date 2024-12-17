def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_set = set(nums)
    max_len = 0
    for n in num_set:
        length = 1
        num = n
        while num + 1 in num_set:
            length += 1
            if length > max_len:
                max_len = length
    return max_len


# print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0]))
