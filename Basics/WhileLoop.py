i = 1
while i < 6:
    print("Number {}".format(i))
    i += 1
else:
    print("Number is no longer less than ")

# Using Break statement
age = 1
while age < 6:
    print("Age {}".format(age))
    # if age is 4, break out of loop
    if age == 4:
        break
    age += 1

# Using continue
year = 2014
while year < 2019:
    # If the year is 2015, increase year and skip the loop for current value
    if year == 2015:
        year += 1
        continue
    print("We won UCL in {}".format(year))
    year += 1
