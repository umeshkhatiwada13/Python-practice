from collections import Counter


def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    cnt = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]
    for chr, freq in cnt.items():
        buckets[freq].append(chr)

    final_str = ''
    for bucket in reversed(buckets):
        for c in bucket:
            final_str += c * int(cnt.get(c))

    return final_str

print(frequencySort('cbbbaa'))
