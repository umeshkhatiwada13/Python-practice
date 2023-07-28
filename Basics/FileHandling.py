import os

if os.path.exists("HelloWorld.txt"):
    print("Append in the existing file")
    my_file = open("HelloWorld.txt", 'a')
    # print(my_file.read())
    my_file.write("\n I am loving it.")
    my_file.close()
    my_file = open("HelloWorld.txt")
    print(my_file.read())
    my_file.close()

    # delete file from the device
    os.remove("HelloWorld.txt")
else:
    print("Create new file")
    file_object = open("HelloWorld.txt", 'x')
    file_object.write("Hello World.\nPython is fun.")
