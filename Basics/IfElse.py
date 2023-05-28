age = 20
if age > 18:
    print("You can vote")

country = "USA"
if country == 'Canada':
    print("You are in Canada")
else:
    print("You are in USA")

employed = False
is_pr = False

if employed and is_pr:
    print("You can lease an apartment")
elif employed or is_pr:
    print("You can lease apartment with additional requirements")
else:
    print("Sorry! you can't lease an Apartment.")
