#loop exercises

#1 - 1 to 10
for x in range(1, 11):
    print(x)

#2 - n to m
print('--------\nDefine your number range:')

x = int(input("Starting #: "))
y = int(input("Ending #: "))

for n in range(x, (y + 1)):
    print(n)

#3 - odd numbers
print('--------\nOnly the odd numbers in your range')

x = int(input("Starting #: "))
y = int(input("Ending #: "))

for n in range(x, (y + 1)):
    if (n % 2 != 0):
        print(n)

#4 - print a square
print('--------\n5 x 5 square')

def stars():
    line = '*****'
    print(line)

stars()
stars()
stars()
stars()
stars()

#5 - print a square II
print('--------\nMake your own square')

star = int(input("How large would you like your square? "))

def stars2():
    line = '*' * star
    print(line)

for x in range(star):
    stars2()
