import numpy as np
import random

#'''
f = lambda x,y: 4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y
dx = lambda x,y: 8*x - 3*y + 24
dy = lambda x,y: -3*x + 4*y - 20
#'''

'''
f = lambda x,y: (1-y)**2 + 100(x-y**2)**2
obj = lambda x: np.power(x, 4)-5*np.power(x, 3)-2*np.power(x, 2)+24*x
seg = (np.sqrt(5)-1)/2
'''

def calculate_gradient(coord):
    x = coord[0]
    y = coord[1]
    return np.array([dx(x,y), dy(x,y)])

def magnitude(array):
    return (array[0]**2 + array[1]**2)

def gradient_descent(lam):
    count = 0
    coord =  np.array([0,0])
    while magnitude(calculate_gradient(coord)) > 0.00000001:
        #print(coord)
        coord = coord - lam *calculate_gradient(coord)
        count += 1
    return coord, count

def golden(f, lower, upper, merror):
    error = 1000
    vals = []
    vals.append((lower+upper)/2)
    objectf = []
    objectf.append(f((lower+upper)/2))
    # you can customize your own condition of convergence, here we limit the error term
    while error >= merror:
        temp1 = upper-seg*(upper-lower)
        temp2 = lower+seg*(upper-lower)
        if f(temp1)-f(temp2)>0:
            upper = temp2
        else:
            lower = temp1
        error = np.abs(f(temp1)-f(temp2))
        vals.append((lower+upper)/2)
        objectf.append(f((lower+upper)/2))
    return (temp2+temp1)/2, f((temp2+temp1)/2), vals, objectf
    

print(gradient_descent(0.1))
print(gradient_descent(0.11))
print(gradient_descent(0.12))
print(gradient_descent(0.13))
print(gradient_descent(0.14))
print(gradient_descent(0.15))
print(gradient_descent(0.16))
print(gradient_descent(0.17))
print(gradient_descent(0.18))
print(gradient_descent(0.19))
print(gradient_descent(0.2))
