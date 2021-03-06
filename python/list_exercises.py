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
matrix1 = [[2, -2], [5, 3]]
matrix2 = [[2, 3], [-1, 0]]
result = [[0, 0], [0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for r in result:
    print(r)

#10 - Matrix Addition II - not clear on how or why this should differ
#from the previous exercise
matrix1 = [[2, -2, 1, 0], [5, 3, 2, 4]]
matrix2 = [[2, 3, 4, 5], [-1, 0, 3, 1]]
result = [[0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for r in result:
    print(r)

#11 - De-dup
list1 = [1, 1, 3, 4, 6, 6, 3, 4, 6]
list2 = (list(set(list1)))

print(list2)
