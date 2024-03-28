import re


def is_palindrome(sent):
    sent = re.sub(r'[^a-zA-Z0-9]+', '', sent).lower()

    print(sent)
    end_index = -1
    for i in range(0, int(len(sent) / 2)):
        print(sent[i])
        print(sent[end_index])
        if sent[i] != sent[end_index]:
            return False
        end_index -= 1
    return True


print(is_palindrome('ab_a'))


def majority_element(nums):
    counter = {}
    for n in nums:
        counter[n] = int(counter.get(n, 0)) + 1

    max_key = max(counter, key=counter.get)

    return max_key


print(majority_element([3, 2, 3]))


def happy_number(num):
    data_map = set()
    while True:
        num_list = []
        while num > 0:
            num_list.append(int(num % 10))
            num = int(num / 10)

        new_num = 0
        for a in num_list:
            new_num += a * a
        if new_num in data_map:
            return False
        if new_num == 1:
            return True
        else:
            data_map.add(new_num)
        num = new_num


num = input("Enter a number : ")
output = happy_number(int(num))
print(output)
if (output):
    print(f'{num} is Happy number')
