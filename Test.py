def read_file(filename):
    number_word_dict = {}
    highest_number = float('-inf')  # Initialize with negative infinity
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                number, word = parts
                number = int(number)
                number_word_dict[number] = word
                if number > highest_number:
                    highest_number = number
    return number_word_dict, highest_number


def get_highest_numbers(num):
    highest_numbers = []
    level = 1
    row_max = 1
    while row_max <= num:
        highest_numbers.append(row_max)
        level += 1
        row_max += level
    return highest_numbers


def decode_message(number_list, number_word_dict):
    decoded_message = ""
    for number in number_list:
        if number in number_word_dict:
            decoded_message += number_word_dict[number] + " "
    return decoded_message.strip()


filename = "encoded_message.txt"
number_word_dict, highest_number = read_file(filename)
number_list = get_highest_numbers(highest_number)
decode_message(number_list, number_word_dict)
