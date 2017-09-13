#List exercises

#1 - Sum the Number
numbers = [8, 5, 12, 31, 32, 12]
print("List: ", numbers)
print(sum(numbers))

#2 - Largest Number
print(max(numbers))

#3 - Smallest Number
print(min(numbers))

#4 - Even Numbers
#evens = [x for x in numbers if x % 2 == 0]
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)
print(evens)

#5 - Positive Numbers - print only positive numbers


#6 - Positive Numbers II - creat a new list with only the positive
positive = []
for x in numbers:
    if x > 0:
        positive.append(x)
print(positive)

#7 - Multiply a list
print(numbers * 2)

#8 - Multiply Vectors
new_numbers = [2, 4, 6, 8, 10, 12]
multiply = []
for x in range(0, len(numbers)):
        z = numbers[x] * new_numbers[x]
        multiply.append(z)
print(multiply)

#9 - Matrix Addition
matrix = [[2, -2], [5, 3]]
result = [[0, 0], [0, 0]]

for i in range(len(matrix)):
    
