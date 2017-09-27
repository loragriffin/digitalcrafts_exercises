
#challenge 1

n = int(input("Number: "))

while n > 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 != 0:
        n = (n * 3) + 1
    # print(int(n))

print(int(n))

#challenge 2 - need to work on this - not working
# num = ''
#
# for x, y in range(100, 1000):
#     z = str(x * y)
#     if z[1:3] == z[3::-1]:
#         num.append(z)
#     # else:
#     #     pass
#
# print(num)

#challenge 3
