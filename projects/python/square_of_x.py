#function exercises

#square of x
import matplotlib.pyplot as plot

def f(n):
    return n * n

x = list(range(-100, 100))
y = []

for n in x:
    y.append(f(n))

plot.plot(x, y)
plot.show()
