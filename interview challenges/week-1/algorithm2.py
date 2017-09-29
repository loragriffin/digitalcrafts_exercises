total = 0

def f(n):
    if n % 3 == 0 or n % 5 == 0:
        return n
    else:
        return 0

for n in range(0, 1001):
    f(n)
    total += f(n)

print(total)
