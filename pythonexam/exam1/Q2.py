# Calculate the discount amount
# Calculate the total amount
RETAIL_PRICE = 299

# Declare user input for quantity
quantity = int(input("Enter the quantity : "))

# Calculate the discount rate
if quantity > 100:
    discountRate = 0.40
elif quantity > 57:
    discountRate = 0.30
elif quantity > 37:
    discountRate = 0.20
elif quantity > 7:
    discountRate = 0.10
else:
    discountRate = 0

# Calculate the full price
full_price = quantity * RETAIL_PRICE
print("Full price before discount : ", full_price)

# Calculate the discount amount
discount_amount = discountRate * full_price
print("Discount rate ", discountRate)
print("Discount amount ", discount_amount)

# Calculate the total amount
total_amount = full_price - discount_amount

print("Total amount after {0} discount : {1}".format(discount_amount, total_amount))
