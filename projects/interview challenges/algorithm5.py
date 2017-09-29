primelist = []

def prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False

i = 2

while len(primelist) < 1000:
    if prime(i) != False:
         primelist.append(i)
    i += 1

# print(primelist)
print(primelist[-1])
