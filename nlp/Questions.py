import re


# Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
def replace_dot_comma_space(input_string):
    # Replace up to 2 occurrences of space, comma, or dot with a colon
    result = re.sub(r'[ ,.]+', ':', input_string, count=2)
    return result


print(replace_dot_comma_space("Hello  This,,is Cristiano Ronaldo."))


# Write a Python program to find all five-character words in a string.
def findLengthFive(inputString):
    wordList = []
    words = inputString.split()
    for word in words:
        if len(word) == 5:
            wordList.append(word)
    return wordList


print(findLengthFive("My name is Cristiano Ronaldo"))