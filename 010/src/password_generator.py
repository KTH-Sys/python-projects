import random

alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers   = list("0123456789")
symbols   = list("!\"#$%&'()*+,-./:;<=>?@[]^_{|}~")

print("Welcome to password generator!")
ur_letter = int(input("How many letters would you like in your password?\n"))
ur_symbol = int(input("How many symbols would you like?\n"))
ur_number = int(input("How many numbers would you like?\n"))

passwordList = []

for n in range(0, ur_letter):
    passwordList.append(random.choice(alphabet))
for n in range(0, ur_symbol):
    passwordList.append(random.choice(symbols))
for n in range(0, ur_number):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)
password = "".join(passwordList)

print(f"Your password is: {password}")
