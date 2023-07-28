# python_file = open("class_task_10.txt")
# print("Reading directly from file: ")
# print(python_file.read())
# python_file.close()
#
# python_file = open("class_task_10.txt")
# writtenLines = python_file.readlines()
# print("Reading line by line from file: ")
# python_file.close()
# # using for loop in the list that store each lines to print all the lines in the file
# for line in writtenLines:
#     print(line)
#
# with open('class_task_10.txt') as file:
#     line_list = []
#     for line in file:
#         line_list.append(line)
#
# print("Storing file in list and reading from file: ")
# print(line_list)
# for line in line_list:
#     print(line)

# python_file = open("class_task_10.txt")
# writtenLines = python_file.readlines()
# print("Reading line by line from file: ")
# # using for loop in the list that store each lines to print all the lines in the file
# for line in writtenLines:
#     print(line.replace("Python", 'Java'))
# python_file.close()

# import os
# guest_name = input("Enter your name: ")
# try:
#     # append if file exists
#     if os.path.exists("guest_name.txt"):
#         guest_file = open("guest_name.txt", 'a')
#     else:
#         # create new file if file doesnot exists
#         guest_file = open("HelloWorld.txt")
#     guest_file.write(guest_name)
#     guest_file.close()
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print("Name written to file successfully.")


# while True:
#     name = input("Enter your name(Type exit to end) :")
#     guest_file = open("guest_name.txt", 'a')
#     if name.lower() == 'exit':
#         # if user input is exit, end the program
#         break
#     print(f"Hello! {name}, Welcome")
#     guest_file.write(name + "\n")

# while True:
#     name = input("Why do you like Programming ? (Type exit to end) :")
#     programming_file = open("programming_file.txt", 'a')
#     if name.lower() == 'exit':
#         # if user input is exit, end the program
#         break
#     print("Thank you! Your response has been recorded.")
#     programming_file.write(name + "\n")

# Open password file
file = open("Passwords.txt")
# declare dictionary to store username-password pair
print("Credentials: ", file.read())
# Open password file
credential_file = open("Passwords.txt")
password_dictionary = dict()  # Dictionary<Username, Password>
for credentials in credential_file:
    # split the line by , to username: $$$ and password: $$$
    credential = credentials.split(",")
    counter = 0
    username = ''
    password = ''
    for c in credential:
        new_data = c.split(":")
        if counter == 0:
            username = new_data[1].strip()
        else:
            password = new_data[1]
            counter = 0
            # store username and password in dictionary
            password_dictionary[username] = password.strip().rstrip()
        counter += 1

# accept user input
username = input("Enter username : ")
password = input("Enter the Password: ")

# validate dictionary has user input username and password for the username
if username in password_dictionary and password_dictionary[username] == password:
    print("User authenticated")
else:
    print("User not authenticated")
