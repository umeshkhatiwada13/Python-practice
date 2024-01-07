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

# Write a Python program to convert a camel-case string to a snake-case string.
def camelToSnakeCase(word):
    wordList = re.findall('[A-Z][a-z]*', word)
    finalWord = ''
    counter = 0
    for w in wordList:
        if counter == 0:
            finalWord += w.lower()
            counter += 1
        else:
            finalWord += '_' + w.lower()
    return finalWord


print(camelToSnakeCase("HelloWorld"))


# Write a python program to convert snake-case string to camel-case string.
def snakeToCamelCase(word):
    wordList = word.split('_')
    finalWord = ''
    for word in wordList:
        finalWord += word.capitalize()
    return finalWord


print(snakeToCamelCase("hello_world"))

# Write a Python program to extract values between quotation marks of a string.
def extractValue(word):
    pattern = re.compile(r'"([^"]*)"')
    return re.findall(pattern, word)


print(extractValue('a"Hello World"'))

# Write a Python program to remove multiple spaces from a string.
def remove_multiple_spaces(text):
    # replacing multiple space with single space
    return re.sub(r'\s+', ' ', text)


print(remove_multiple_spaces("Hello World. I  am    a Python programmer"))
