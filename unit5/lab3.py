
# Dice Simulator Using Random Module

import random

print("===== DICE SIMULATOR =====")

while True:
    print("\n1. Roll Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = random.randint(1, 6)

        print("\nRolling the dice...")
        print("You got:", number)

    elif choice == "2":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice! Try again.")
