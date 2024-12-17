def count_and_say(nums):
    if not nums:
        return ''

    num_array = list(nums)
    last_num = num_array[0]
    count = 0
    final_num = ''
    for n in num_array:
        if last_num != n:
            final_num += str(count) + str(last_num)
            last_num = n
            count = 1
        else:
            count += 1
    final_num += str(count) + str(last_num)
    return final_num


print(count_and_say('3322251'))
