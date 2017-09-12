# guess the number

import random
number = random.randint(1, 10)
count = 5

print("I am thinking of a number between 1 and 10.\nYou get {} guesses.".format(count))
guess = int(input("What's the number? "))

while guess != number:
    if guess < number:
        count -= 1
        print("{} is too low. Try again.\nYou have {} guesses left.".format(guess, count))
    if guess > number:
        count -= 1
        print("{} is too high. Try again.\nYou have {} guesses left.".format(guess, count))
    guess = int(input("What's the number? "))
    if guess == number:
        print("You got it! You win!")
    if count == 0:
        break
        print("You ran out of guesses!")
