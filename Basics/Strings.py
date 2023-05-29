# declare string
word = 'Hello World'

# loop through word
for a in word:
    print(a)

# print ith element
print("0th element of word", word[0])

# print element from i to jth index
print("Letter from 0th to 7th index", word[0:7])

# print last letter of the word
print("Last letter of word ", word[-1])

# Upper case
print("Upper {0}".format(word.upper()))

# Lower case
print("Lower {0}".format(word.lower()))

# String length
print("Length {}".format(len(word)))

# Multiline String
multiline = ''' Hello World
            Hello World'''
print("Multiline string : {}".format(multiline))

wordSplit = " Hello,World "
# Remove whitespace
print("Word after trim : {}".format(wordSplit.strip()))

# Split
print("Word after split with , : ", wordSplit.strip().split(","))
