def count_and_say(num):
    prev_num = ''
    num_count = 1
    final_string = ''
    for n in str(num):
        if prev_num != n:
            final_string += str(num_count) + str(n)
            prev_num = ''
        else:
            prev_num = str(n)
            num_count += 1

    return final_string


print(count_and_say(3322251))
