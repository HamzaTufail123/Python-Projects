##   Number Trick Game  ##

import random

print("🎲 Welcome to the Number Trick Game!")
print("Step 1: Think of a number for yourself (don't tell anyone).")
your_number = int(input("Enter your number (e.g. 4): "))

print("-" * 30)
print(f"Step 2: Use the same number like: {your_number} for your father.")
father_number = int(input("Enter your father's number (same as yours): "))

print("-" * 30)
computer_number = random.randint(1, 10)
print(f"Computer secretly chose a number: {computer_number}")

sum_all = your_number + father_number + computer_number
print(f"\n🔢 Total sum: {your_number} + {father_number} + {computer_number} = {sum_all}")

print("-" * 30)
charity = sum_all / 2
print(f"🤲 You gave half in charity: {charity}")

print("-" * 30)
returned = charity - father_number
print(f"👨‍👧 You returned father's number: {father_number}")
print(f"💡 What's left with you: {returned}")

print("-" * 30)
print(f"🎯 Surprise! The answer is always half of computer's number: {computer_number / 2}")
