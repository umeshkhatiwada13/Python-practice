def find_product(array):
    final_array = [0] * len(array)
    index_a = 0
    for a in array:
        product = 1
        print(a)
        index_b = 0
        for b in array:
            if index_a == index_b:
                index_b += 1
                continue
            product = product * b
            index_b += 1
        final_array[index_a] = product
        index_a += 1

    return final_array


print(find_product([1, 2, 4, 6]))
print(find_product([-1, 0, 1, 2, 3]))
