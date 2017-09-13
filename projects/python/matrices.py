#Notes from lecture

#8 Multiply Vectors
#[2, 4, 5] * [2, 3, 6] = [4, 12, 30]
m1 = [2, 4, 5]
m2 = [2, 3, 6]

#wrong way - overcomplicated... only need one loop
#loop inside a loop is exponential
answer = []
for num1 in m1:
    for num2 in m2:
        answer.append(num1 * num2)

print(answer)

#correct way
answer = []
for i in range(0, len(m1)):
    answer.append(m1[i] * m2[i])

print(answer)

#another way of writing the solution above
for i in range(0, len(m1)):
    ans = m1[i] * m2[i]
    answer.append(ans)

print(answer)

#another correct way - using built in function (enumerate)
answer = []

for i, num1 in enumerate(m1):
    answer.append(num1 * m2[i])

print(answer)
