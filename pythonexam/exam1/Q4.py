# take starting_weight as input from user
starting_weight = float(input("What is your starting weight?"))
# assign starting_weight to new variable for calculation
weight = starting_weight
print("Your initial weight : {0}".format(weight))
for month in range(1, 7):
    weight -= 4
    print("At end of Month {0}, Your weight will be {1}".format(month, weight))

print("Your initial weight was {0} and your final weight is {1}".format(starting_weight, weight))
