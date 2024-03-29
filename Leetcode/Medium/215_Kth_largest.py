# solved using basic approach in O(nlogn) time complexity
a = [3, 2, 1, 5, 6, 4]

def kth_largest(num_list, k):
    a_s = sorted(num_list)
    print(reversed(a_s))
    count = 1
    k = 2
    for a in reversed(a_s):
        if k == count:
            return a
        else:
            count += 1


print(kth_largest(a, 2))
