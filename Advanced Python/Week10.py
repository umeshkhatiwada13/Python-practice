def count_and_say(n):
    if n == 1:
        return '1'

    prev_term = count_and_say(n - 1)
    result = ''
    count = 1

    for i in range(len(prev_term)):
        if i < len(prev_term) - 1 and prev_term[i] == prev_term[i + 1]:
            count += 1
        else:
            result += str(count) + prev_term[i]
            count = 1

    return result


n = int(input("Enter the nth number : "))
print(count_and_say(n))


def multiply_strings(num1, num2):
    # Initialize result list with zeros
    result = [0] * (len(num1) + len(num2))

    # Perform multiplication
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            mul = int(num1[i]) * int(num2[j])
            pos1, pos2 = i + j, i + j + 1
            total = mul + result[pos2]
            result[pos1] += total // 10
            result[pos2] = total % 10

    # Remove leading zeros
    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    # Convert result to string
    return ''.join(map(str, result))


n1 = input("Enter first number : ")
n2 = input("Enter second number : ")
print(multiply_strings(n1, n2))
