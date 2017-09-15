#function exercises

#1 - hello
name = input('What is your name? ')

def hello(name):
    print('Hello, ', name, '. It\'s nice to meet you.')

hello(name)


#2 - y = x + 1
import matplotlib.pyplot as plot

def f(x):
    return x + 1

xs = list(range(-3, 4))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
