# 3 Guests invited to Dinner
guestList = ["Ramos", "Kroos", "Ronaldo"]

# Printing Invitation Message
for i in guestList:
    print("Dear {} ,I would like you to invite to Sunday Dinner. Hope to see you there.".format(i))

# Printing Original Guest List
print("Original Guest length : {}".format(len(guestList)))

# Ronaldo can't make it
print("{} wont be there.".format(guestList[2]))

# Inviting Benzema instead
guestList[2] = "Benzema"

# Printing Guest List after changing replacing one member
print("Guest list after replacing Ronaldo with Benzema : {}".format(len(guestList)))

# New Invitation including Benzema
for i in guestList:
    print("Dear {} ,I would like you to invite to Sunday Dinner. Hope to see you there.".format(i))

# Room for 3 more Guest Available
print("Good news, I got bigger table. I can invite 3 more Guests.")
guestList.insert(0, "Courtious")
guestList.insert(3, "Vini")
guestList.append("Lucas")

# Printing List after adding 3 more Guests
print("List after adding 3 more Guests : {}".format(len(guestList)))

# new Invitation message
for guest in guestList:
    print("Dear {} ,I would like you to invite to Sunday Dinner. Hope to see you there.".format(guest))

print("Bad news, The table won't be ready on time.")
print("Removing other guests from list leaving 2 guests only")
# Removing the guest leaving 2 guest using loop
for guest in range(2, len(guestList)):
    print("Sorry {}, I will invite you next time.".format(guestList.pop()))

# Printing Guest List after removing 4 guests
print("Guest List after uninviting 4 guests : {}".format(len(guestList)))

print("Printing Reminder invitation message to remaining 2 guests.")
# Printing Reminder message to remaining 2 guests
for guest in guestList:
    print("Hello {}, You are still invited.".format(guest))

# Removing 2 guests using del
del guestList[1]
del guestList[0]

print("List after deleting all guests : {}".format(guestList))
