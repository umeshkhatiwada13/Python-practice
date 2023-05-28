placesToVisit = ["Madrid", "Rome", "Goa", "Cairo", "New York"]

print("Places I want to visit")
for place in placesToVisit:
    print(place)

# Sorting the new list
placesToVisitSorted = sorted(placesToVisit)
print("New Alphabetically sorted list : {}".format(placesToVisitSorted))

# Printing Original List
print("Original list : {}".format(placesToVisit))

# Using sorted() function to print original list
print("Sorting the Original List: {}".format(sorted(placesToVisit)))

# Original List is not changed after using sorted function
print("Original list ", placesToVisit)

# Reversing the original list alphabetically
placesToVisit.reverse()
print("Order of original list {} after reverse()".format(placesToVisit))

# Re-Reversing the list alphabetically or changing the data to original list
placesToVisit.reverse()
print("Order of original list {} after 2 reverse()".format(placesToVisit))

# Sorting the data alphabetically
placesToVisit.sort()
print("Sorting Original list in Alphabetic order {}".format(placesToVisit))

# Sorting the data alphabetically in reverse order
placesToVisit.sort(reverse=True)
print("Sorting Original list in reverse Alphabetic order {}".format(placesToVisit))
