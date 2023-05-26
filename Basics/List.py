fruitList = ["apple", "banana", "cherry", "grape", "orange"]

# loop through fruit list
for fruit in fruitList:
    print(fruit)

# print using comprehension 
[print(x) for x in fruitList]

# print first 3 element in fruit list
print("First 3 element of list ", fruitList[0:3])

# print last element in fruit list
print("Last element of the list ", fruitList[-1])

# print list lenght
print("Length of list ", len(fruitList))

# check if item exist in the list
if 'apple' in fruitList:
    print("Apple is present in list")

# change 3rd item of  the list
fruitList[3] = 'new grape'
print("List after item change in 3rd index ", fruitList)

# add new item at last index
fruitList.append("guava")
print("List after appending guava ", fruitList)

# remove item from last index
print("List after removing item ", fruitList.pop())
print(fruitList)

# remove item by name
fruitList.remove("new grape")
print('list after removing new grape {}'.format(fruitList))

# remove item using del
del fruitList[3]
print("List after removing item at 3rd index ", fruitList)
