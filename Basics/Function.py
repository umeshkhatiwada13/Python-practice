# Simple function
def printText():
    print("Hello world")


# calling the function
printText()


# Function with parameter
def chatBot(name):
    print("Hello {}, I am chatbot".format(name))


# Calling the function and passing parameter
chatBot("Ram")


# Function with parameter and returntype
def sum(num1, num2):
    return num1 + num2


addition = sum(2, 4)
print("Result is {}".format(addition))
