# guess the number

number = 5
print("I am thinking of a number between 1 and 10.")
guess = int(input("What's the number? "))

while guess != 5:
    if guess < 5:
        print("{} is too low. Try again.".format(guess))
    if guess > 5:
        print("{} is too high. Try again.".format(guess))
    guess = int(input("What's the number? "))
if guess == 5:
    print("You got it! You win!")
