import random

print("----- NUMBER GUESSING GAME -----")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed correctly.")
        print("Number of attempts:", attempts)
        break
