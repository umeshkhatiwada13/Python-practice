def encode(strs):
    final_str = ''
    for s in strs:
        final_str += str(len(s)) + '#' + s
    return final_str


def decode(str):
    if len(str) == 0:
        return []
    index = 0
    str_list = []
    separator = '#'
    while True:
        num = int(str[index])
        if str[index + 1] == separator:
            index = index + 2
            str_list.append(str[index: index + num])
            if index + num >= len(str):
                break
            index = index + num

    return str_list


encoded_str = encode(['Hello', 'World', 'I', 'am', 'Umesh'])
print(encoded_str)
print(decode(encoded_str))

import time


def test_encode_decode(test_cases):
    for i, test_case in enumerate(test_cases):
        print(f"Test Case {i + 1}:")
        print("Input:", test_case)

        # Encode
        start_time = time.time()
        encoded_str = encode(test_case)
        encode_time = time.time() - start_time
        print("Encoded:", encoded_str[:10], "..." if len(encoded_str) > 10 else "")
        print("Encode Time Elapsed:", encode_time, "seconds")

        # Decode
        start_time = time.time()
        decoded_str = decode(encoded_str)
        decode_time = time.time() - start_time
        print("Decoded:", decoded_str[:10], "..." if len(decoded_str) > 10 else "")
        print("Decode Time Elapsed:", decode_time, "seconds")

        print("-" * 40)


# Test Cases
test_cases = [
    ["abc", "def", "ghi"],
    ["hello", "world"],
    # ["a" * 10 ** 6, "b" * 10 ** 6, "c" * 10 ** 6],
    # ["x" * 10 ** 7, "y" * 10 ** 7, "z" * 10 ** 7],
    [],
    [""],
    ["$", "#", "%"],
    ["!@#", "&*()"]
]

test_encode_decode(test_cases)
