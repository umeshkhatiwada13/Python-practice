def merge_sorted_array(a, b):
    temp = int(-2 ** 32)
    j = 0
    for i in range(0, len(a)):
        if (temp > a[i]):
            a[i] = temp
            temp = int(-2 ** 32)
        elif (a[i] > b[j]):
            temp = a[i]
            a[i] = b[j]
            j = j + 1
        elif (a[i] < b[j]):
            continue
    return a


print(merge_sorted_array([1, 2, 3, 0, 0, 0], [2, 5, 6]))

a = [1,2,3]
for i, n in enumerate(a):
    print(i, n)
