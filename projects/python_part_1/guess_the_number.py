# guess the number

import random
number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")
guess = int(input("What's the number? "))

while guess != number:
    if guess < number:
        print("{} is too low. Try again.".format(guess))
    if guess > number:
        print("{} is too high. Try again.".format(guess))
    guess = int(input("What's the number? "))
if guess == number:
    print("You got it! You win!")
