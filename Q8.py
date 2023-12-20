# Quasion 8
charge = float(input("Enter the charge for the food: "))
tip = charge * 0.15
tax = charge * 0.07
total = charge + tip + tax
print(f"The amount of a 15 percent tip is: {tip}")
print(f"The amount of a 7 percent sales tax is: {tax}")
print(f"The total amount of a meal is: {total}")
