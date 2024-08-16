"""1.  Using  a  for  loop,  simulate  rolling  a  sixsided  die  multiple  times  (at  least  20times).   Count and print the following statistics:   How many times you rolled a 6   How many times you rolled a 1   How many times you rolled two 6s in a row"""

import random

# ----- Set the number of rolls ----- #
num_rolls = 20

# ----- Initialize counters for specific roll values and two consecutive 6s ----- #
num_rolls_6 = 0
num_rolls_1 = 0
consecutive_6s = 0

# ----- Initialize previous roll value ----- #
prev_roll = 0
for _ in range(num_rolls):
    # ----- Simulate a dice roll ----- #

    dice_roll = random.randint(1, 6)
    # dice_roll = int(input("Enter dice number: "))
    print(dice_roll, end=" ")

    # ----- Increment the counter if the roll is a 6 or 1 ----- #
    if dice_roll == 6:
        num_rolls_6 += 1

    elif dice_roll == 1:
        num_rolls_1 += 1

    # ----- Check if two 6s have been rolled consecutively ----- #
    if prev_roll == 6 and dice_roll == 6:
        consecutive_6s += 1


    prev_roll = dice_roll

# ----- Print the number of times each event occurred during the specified number of rolls ----- #
print(f"\nNumber of times rolled a 6: {num_rolls_6}")
print(f"Number of times rolled a 1: {num_rolls_1}")
print(f"Number of times rolled two 6s in a row: {consecutive_6s}")

# ----- Exit Program ----- #
exit()
