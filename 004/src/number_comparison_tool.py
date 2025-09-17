#003 Number Comparison Tool

#Step 1: Ask for the user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Step 2: Compare the numbers
if num1 == num2:
  print("Both numbers are equal")
elif num1 < num2:
  print(f"{num2} is greater than {num1}")
else:
  print(f"{num1} is greater than {num2}")

#Check zero
if num1 == 0 or num2 == 0:
  print("At least one number is zero.")
else:
  print("Both numbers are non-zero numbers.")
