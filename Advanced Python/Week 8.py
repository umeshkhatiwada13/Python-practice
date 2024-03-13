def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs.sort()
    l_substr = ''
    first_element = strs[0]
    last_element = strs[-1]
    for i in range(len(first_element)):
        if first_element[i] == last_element[i]:
            l_substr += first_element[i]
        else:
            break
    return l_substr


print(longestCommonPrefix(['flower', 'flight', 'flow']))


def majority_element(nums):
    counter = {}
    for n in nums:
        counter[n] = int(counter.get(n, 0)) + 1

    max_key = max(counter, key=counter.get)

    return max_key

print(majority_element([3,2,3]))





