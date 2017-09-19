#json exercise

import json
import matplotlib.pyplot as plot

plot_points = {'data' : [
    [1, 3],
    [2, 3],
    [3, 5],
    [4, 5]
]}
with open('points.json', 'w') as fh:
    json.dump(plot_points, fh)

with open('points.json', 'r') as fh:
    plot_points = json.load(fh)

points = plot_points['data']

x = [row[0] for row in points]
y = [row[1] for row in points]

print(x)
print(y)

plot.plot(x, y)
plot.show()
