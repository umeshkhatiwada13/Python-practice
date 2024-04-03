def add_to_array(nums):
    n_str = ''
    for n in nums:
        n_str += str(n)
    n_int = int(n_str) + 1
    n_new = []
    for s in str(n_int):
        n_new.append(int(s))

    return n_new


print(add_to_array([1, 2, 3, 4]))
