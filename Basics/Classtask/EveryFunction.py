# Initalizing list of river
riverList = ['Amazon', "Nile", "Bagmati"]

# print list length
print("Length of list ", len(riverList))

# add new item at last index
riverList.append("Sindhu")
print("List after appending Sindhu ", riverList)

# change 3rd item of  the list
riverList[3] = 'Gangas'
print("List after changing Gangas in 3rd index ", riverList)

# sort the list
riverList.sort()
print("List after sorting {}".format(riverList))

# sort the list
riverList.reverse()
print("List after reversing {}".format(riverList))

# remove item from last index
print("List after removing item ", riverList.pop())
print(riverList)

# clear the list
riverList.clear()
print("List after clearing {} ".format(riverList))
