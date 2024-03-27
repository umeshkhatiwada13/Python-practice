# if there are n unique elements in the list, the first n numbers should be those
# unique numbers and the numbers after n doesnot matters
# return the length of those unique elements
# reflect the change in original array ( do not create a second array)
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    index = 0
    val = -int(2 ** 31)
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            val = nums[index]
            index = index + 1
    # returns the number of unique element
    return index


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
