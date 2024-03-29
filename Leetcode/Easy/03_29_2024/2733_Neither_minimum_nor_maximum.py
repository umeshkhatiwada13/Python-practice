def findNonMinOrMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n_unique = []
    last_num = 0
    for n in nums:
        if last_num == n:
            continue
        n_unique.append(n)
        last_num = n

    if len(n_unique) <= 2:
        return -1

    n_sorted = sorted(n_unique)

    num_list = [a for a in n_sorted]
    return num_list[1]


print(findNonMinOrMax([2, 4, 25]))
