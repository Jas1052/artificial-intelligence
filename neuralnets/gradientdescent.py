import numpy as np
import random

f = lambda x,y: 4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y
dx = lambda x,y: 3*x - 3*y -24
dy = lambda x,y: -3*x + 3*y -20

def calculate_gradient(coord):
    x = coord[0]
    y = coord[1]
    return np.array(dx(x, y), dy(x, y))

def magnitude(array):
    return (array[0]**2 + array[1]**2)

def gradient_descent(val):
    coord = np.array([0, 0])
    while magnitude(calculate_gradient(coord)) > 0.00000001:
        coord = coord - val * calculate_gradient(coord)
    return coord

print(gradient_descent(0.1))
