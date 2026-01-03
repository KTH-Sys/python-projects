import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
usage = [rock, paper, scissors]
if 0 <= choice <= 2:
    print(usage[choice])
else:
    print("Invalid Number!")
    exit()

comp_choice = random.randint(0,2)
output = usage[comp_choice]
print(f"Computer chose: {output}")

if choice == comp_choice:
    print("Tie")
elif (choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1):
    print("You win!")
else:
    print("You lose!")
