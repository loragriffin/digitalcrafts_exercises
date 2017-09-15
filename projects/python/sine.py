#function exercises
#5 - sine
from math import sin
import matplotlib.pyplot as plot
from numpy import arange

x = list(arange(-5, 5, 0.1))
y = []

for n in x:
    y.append(sin(n))

plot.plot(x, y)
plot.show()
