#function exercises
#4 - odd or even

import matplotlib.pyplot as plot

def f(n):
    if n % 2 == 0:
        return -1
    if n % 2 != 0:
        return 1

x = list(range(-5, 5))
y = []

for n in x:
    y.append(f(n))

plot.bar(x, y)
plot.show()
