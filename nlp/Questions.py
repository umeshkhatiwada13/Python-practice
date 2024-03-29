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

# Write a Python program to remove all whitespaces from a string.
def remove_whitespaces(text):
    return text.replace(" ", '')


print(remove_whitespaces("Hello World. I am a Python programmer"))

# Write a Python program to find URLs in a string.
def extract_urls(sentence):
    urls = re.findall(r'https?://\S+|www\.\S+', sentence)
    return urls


print(extract_urls(
    "Hello. I am Cristiano Ronaldo. Find me at https://cristianoronaldo.com or https://allnassr.com/ronaldo"))


# Write a Python program to split a string into uppercase letters.
def uppercase_letters(string):
    uppercase_letter_list = []
    for char in string:
        if (char.isupper()):
            uppercase_letter_list.append(char)
    return uppercase_letter_list


print(uppercase_letters("Hello World. I am a Python"))

# Write a Python program to do case-insensitive string replacement.
def case_insensitive_replace(input_string, target, replacement):
    result = re.sub(re.escape(target), replacement, input_string, flags=re.IGNORECASE)
    return result


print(case_insensitive_replace("I am Cristiano", "Cristiano", "cristiano"))

# Write a Python program to insert spaces between words starting with capital letters.
def replace_capital_by_space(string):
    pattern = re.compile(r'([a-z])([A-Z])')
    return re.sub(pattern, r'\1 \2', string)


print(replace_capital_by_space("HelloThisIsCristianoRonaldo"))
