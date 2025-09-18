#005: Countdown Timer

import time

# Step 1: User Input
start = int(input("What number do you want to start counting?"))

# Step 2: Loop the countdown
print("\n ----Welcome to the countdown timer!-----")
while start > 0:
  print(start)
  time.sleep(1)
  start -= 1
print("Countdown successfully complete!")
