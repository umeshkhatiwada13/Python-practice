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

# Write a Python program to find all three, four, and five character words in a string.

def findGivenWords(inputString):
    wordList = []
    words = inputString.split()
    for word in words:
        if len(word) == 5 or len(word) == 4 or len(word) == 3:
            wordList.append(word)
    return wordList


print(findGivenWords("My name is Cristiano"))

# Write a Python program to find all words that are at least 4 characters long in a string.
def getWords(inputString):
    wordList = []
    words = inputString.split()
    for word in words:
        if len(word) >= 4:
            wordList.append(word)
    return wordList


print(getWords("My name is Cristiano"))