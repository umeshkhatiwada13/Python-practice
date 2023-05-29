# Second parameter refers to what operation we want to perform with the file
# r - read , w - write , a - append, w+ - read and write
test_file = open("Test.txt", "r")
# checks if the file is readable
# readable for r and w+, false for other operations
print("Is file readable {}".format(test_file.readable()))

# Read the whole file at one go
print(test_file.read())

# read the first line and push the cursor to start of second line
print(test_file.readline())

# Read all lines in the file , the lines are stored in list using readLines() command
print(test_file.readlines())

writtenLines = test_file.readlines()
# using for loop in the list that store each lines to print all the lines in the file
for line in writtenLines:
    print(line)

test_file.close()
