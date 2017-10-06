# How many coins?

coins = 0
print("You have {} coins.".format(coins))
another = input("Do you want another coin? (yes/no) ")
another = another.lower()

while another == 'yes':
    coins += 1
    print("You have {} coins.".format(coins))
    another = input("Do you want another coin? (yes/no) ")
    another = another.lower()

print("Bye!")
