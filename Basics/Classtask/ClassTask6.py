fruit = 'apple'
print("Is fruit == 'apple'? I predict true")
print(fruit == 'apple')
print("Is fruit == 'banana'? I predict false")
print(fruit == 'banana')

pizza = 'cheese'
print("Is pizza == 'cheese'? I predict true")
print(pizza == 'cheese')
print("Is pizza == 'veggie'? I predict false")
print(pizza == 'veggie')

game = 'football'
print("Is game == 'football'? I predict true")
print(game == 'football')
print("Is game == 'golf'? I predict false")
print(game == 'golf')

city = 'Toronto'
print("Is city == 'Toronto'? I predict true")
print(city == 'Toronto')
print("Is city == 'BC'? I predict false")
print(city == 'BC')

drink = 'Fanta'
print("Is drink == 'Fanta'? I predict true")
print(drink == 'Fanta')
print("Is drink == 'Coke'? I predict false")
print(drink == 'Coke')

weather = 'Fall'
print("Is weather == 'Fall'? I predict true")
print(weather == 'Fall')
print("Is weather == 'Summer'? I predict false")
print(weather == 'Summer')

# declare list for string comparison in loop
seafood_list = ["shrimp", "oysters"]
food_list = ["pizza", "chicken", "oysters", "shrimp"]

# check if the item is in seafood_list
for food in food_list:
    # using lower to check string equality
    print(f"Is {food} a seafood?  {food.lower() in seafood_list}")

# test for equality and inequality with string
weather = 'Fall'
weatherS = 'summer'
print(f"are {weather} and {weatherS} same? {weatherS == weather}")

sunny = True

# use and,or operator for string comparison
if weatherS == 'summer' and sunny:
    print("Let's go for Swimming")
elif weatherS == 'summer' or sunny:
    print("Let's go for Picnic.")
else:
    print("Lets stay in Home")


# function to print points message
def alien_shooter(color):
    if color == 'green':
        return "Congrats! You have earned 5 Points."
    elif color == 'yellow':
        return "Congrats! You have earned 10 Points."
    else:
        return "Congrats! You have earned 15 Points."


# condition for green alien
print("Alien Color was Green ", alien_shooter('green'))
# condition for yellow alien
print("Alien Color was Yellow ", alien_shooter('yellow'))
# condition for red alien
print("Alien Color was Red ", alien_shooter('red'))

# take age as input from user
age = int(input("Enter your age: "))

# else if conditions
if age < 2:
    print("You are a Baby")
elif age >= 2 and age < 4:
    print("You are a Toddler")
elif age >= 4 and age < 13:
    print("You are a Kid")
elif age >= 13 and age < 20:
    print("You are a Teen")
elif age >= 20 and age < 65:
    print("You are an Adult")
else:
    print("You are an Elder")

# declare list of favorite fruits
favorite_fruits = ['banana', 'mango', 'grape']

# check if the fruit is in favorite food list
if 'Apple'.lower() in favorite_fruits:
    print("I really like Apple")
if 'Orange'.lower() in favorite_fruits:
    print("I really like Orange")
if 'Banana'.lower() in favorite_fruits:
    print("I really like Banana")
if 'Grape'.lower() in favorite_fruits:
    print("I really like Grape")
if 'Kiwi'.lower() in favorite_fruits:
    print("I really like Kiwi")
