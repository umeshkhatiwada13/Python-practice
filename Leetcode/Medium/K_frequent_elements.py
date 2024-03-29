from collections import Counter


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    cnt = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in cnt.items():
        buckets[freq].append(num)

    res = []
    for bucket in reversed(buckets):
        for num in bucket:
            res.append(num)
            if len(res) == k:
                return res


print(topKFrequent([1], 1))
