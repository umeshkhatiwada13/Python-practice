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

# print list length
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

# find index of the item
print("Index of guava is ", fruitList.index("guava"))

# remove item from last index
print("List after removing item ", fruitList.pop())
print(fruitList)

# remove item by name
fruitList.remove("new grape")
print('List after removing new grape {}'.format(fruitList))

# copy list to new list (shallow copy), only copy the reference, both lists will reference to the same list
# in memory
fruitListCopy = fruitList
# copy list to new list (deep copy) , copy the elements and doesn't reference the old list
fruitListDeepCopy = fruitList.copy()
print("Shallow Copy new list {}".format(fruitListCopy))

# when item is removed from original list, it also effects the copied list
fruitList.remove("banana")
print("Shallow copied after removing banana", fruitListCopy)
print("Deep copied after removing banana", fruitListDeepCopy)

# sort item in list
fruitList.sort()
print('List after sorting {}'.format(fruitList))

# remove item using del
del fruitList[3]
print("List after removing item at 3rd index ", fruitList)

# repeat the list n times
repeatedFruitList = fruitList * 3
print("Repeated fruit list ", repeatedFruitList)

# join two list
joinFruitList = repeatedFruitList + fruitList
print("Joined fruit list ", joinFruitList)

# clear the list
fruitList.clear()
print("List after clearing {} ".format(fruitList))
