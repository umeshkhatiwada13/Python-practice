# declare dictionary
footballers = {
    "Ramos": 4,
    "Carvajal": 2,
    "Alaba": 5,
    "Kroos": 8
}

# print the type
print("Type of the Object {}".format(type(footballers)))

# print the dictionary
print("Dictionary is {}".format(footballers))

# print the keys
print("Keys of the dictionary {}", footballers.keys())

# print the values
print("Value of the dictionary {}", footballers.values())

# add new element to the dictionary
footballers["Modric"] = 10

print("Dictionary after adding Modric ", footballers)

# change value of an item
footballers['Alaba'] = 3
print("Dictionary after changing Jersy number of Alaba {}".format(footballers))

# delete item from dictionary
del footballers["Ramos"]
print("Dictionary after deleting Ramos {}".format(footballers))

# getOrDefault for dictionary
print("Get Ramos if present else print Captain : ", footballers.get("Ramos", "Captain"))

# removing random item
print("Dictionary after removing random element ", footballers.popitem())


