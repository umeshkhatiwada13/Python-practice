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


def count_good_subsets(nums):
    MOD = 10 ** 9 + 7
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    # Count occurrences of each number in nums
    count = [0] * 51
    for num in nums:
        count[num] += 1

    # Initialize dp array
    dp = [0] * 51
    dp[1] = 1

    # Calculate dp values
    for prime in primes:
        for num in range(prime, 51, prime):
            dp[num] += count[num] * dp[prime]
            dp[num] %= MOD

    # Special handling for multiples of 2, 3, 5, 7 since they can form multiple good subsets
    total = sum(count)
    for i in range(2, 51):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total -= count[i]

    return (pow(2, total, MOD) * dp[1]) % MOD


# Take input from the user
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

print(nums)

# Call the function and print the result
print(count_good_subsets(nums))

