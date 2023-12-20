# Quasion 6
purchase_amount = float(input("Enter the amount of a purchase: "))
state_tax = purchase_amount * 0.04
county_tax = purchase_amount * 0.02
total_tax = state_tax + county_tax
total_sale = purchase_amount + total_tax
print(f"The amount of the purchase is: {purchase_amount}")
print(f"The state sales tax is: {state_tax}")
print(f"The county sales tax is: {county_tax}")
print(f"The total sales tax is: {total_tax}")
print(f"The total of the sale is: {total_sale}")
