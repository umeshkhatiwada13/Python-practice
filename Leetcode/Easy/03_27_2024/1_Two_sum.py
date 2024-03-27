def twoSum(nums, target):
    smap = {}
    for i, n in enumerate(nums):
        smap[target - n] = i

    for i, n in enumerate(nums):
        if (n in smap):
            return [i, smap[n]]


print(twoSum([3,2,4], 6))
