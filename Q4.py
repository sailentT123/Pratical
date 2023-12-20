# Quasion 4
total = 0
for i in range(5):
    price = float(input(f"Enter the price of item {i+1}: "))
    total += price
tax = total * 0.06
total += tax
print(f"The subtotal of the sale is: {total-tax}")
print(f"The amount of sales tax is: {tax}")
print(f"The total is: {total}")
