from math import exp, sqrt
primelist = []

def prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False

#y = 13195
y = 600851475143

for i in range(2, int(sqrt(y))):
    if y % i == 0 and prime(i) != False:
         primelist.append(i)

print(primelist)
print(primelist[-1])
