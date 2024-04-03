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
        while True:
            length += 1
            num = num + 1
            if length > max_len:
                max_len = length
            if num + 1 not in num_set:
                break
    return max_len


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
