print("Welcome to the Tip Calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

cost = (total * (tip / 100) + total) / people
print(f"Each person should pay: {cost}")
