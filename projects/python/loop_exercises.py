#loop exercises

#1 - 1 to 10
for x in range(1, 11):
    print(x)

#2 - n to m
x = int(input("Starting #: "))
y = int(input("Ending #: "))

for n in range(x, (y + 1)):
    print(n)

#3 - odd numbers
x = int(input("Starting #: "))
y = int(input("Ending #: "))

for n in range(x, (y + 1)):
    if (n % 2 != 0):
        print(n)

#4 - print a square
