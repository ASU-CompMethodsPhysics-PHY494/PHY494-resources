# guess.py

import random

number = random.randint(1, 1000)  # secret integer number between 1 and 1000

n_guesses = 0
guess = int(input("Guess the number between 1 and 1000: "))

while guess != number:
    n_guesses += 1
    if guess > number:
        print(guess, "is too high")
    elif guess < number:
           print(guess, "is too low")
    guess = int(input("Guess again: "))

print("Congratulations, you guessed the number", number, "in", n_guesses, "guesses")
