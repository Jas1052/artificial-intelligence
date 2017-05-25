import numpy as np
import itertools
import copy
import math
import random

#classes defined: Percept and Input(extends Percept)
#parameters: the weights (w_ij) and thresholds (t_j)

class Percept:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
        self.percepts = None
    def set_inputs(self, percepts):
        self.percepts = percepts
    def actuator(self, value):
        val = 1/(1+math.e**(-5 * value))
        if val > self.threshold:
            return 1
        else:
            return 0
        # return 1 if val > self.threshold else 0
        
    def evaluate(self):
        total = 0
        for index in range(len(self.percepts)):
            total += self.weights[index] * self.percepts[index].evaluate()
        return self.actuator(total)

class Input(Percept):
    def __init__(self):
        self.value = None
    def set_value(self, val):
        self.value = val
    def evaluate(self):
        return self.value

x1 = Input()
x2 = Input()

node_1 = Percept([0,-1],-1) # nand
node_2 = Percept([0, 1], -1) # or
node_3 = Percept([1, 0], -1) # and 
node_4 = Percept([-1, 0], -1) # nor

node_1.set_inputs([x1, x2])
node_2.set_inputs([x1, x2])
node_3.set_inputs([x1, x2])
node_4.set_inputs([x1, x2])

node_1and2 = Percept([1, 1], 1.5)
node_3and4 = Percept([1, 1], 1.5)

node_1and2.set_inputs([node_1, node_2])
node_3and4.set_inputs([node_3, node_4])

node_h = Percept([1, 1], 1.5)
node_h.set_inputs([node_1and2, node_3and4])

cc = node_h

ac = 0
for i in range(10000):
    x = random.uniform(-1.5, 1.5)
    y = random.uniform(-1.5, 1.5)
    x1.set_value(x)
    x2.set_value(y)
    if (x*x + y*y) <= 1 and cc.evaluate() ==1 or (x*x + y*y) >=1 and cc.evaluate() == 0:
        ac = ac + 1

print(ac/100)

"""
values = [[-0.5, -0.5, -1.5],
[ 0.5,  0.5, -0.5],
[ 1.5, -2.5, -0.5],
[ 1.5,  0.5, -0.5],
[-1.5,  1.5, -0.5],
[-0.5,  1.5, -0.5],
[ 1.5,  1.5, -0.5],
[-0.5, -0.5,  0.5],
[ 0.5, -1.5,  0.5],
[ 1.5, -0.5,  0.5],
[-2.5,  0.5,  1.5],
[-0.5,  1.5,  0.5],
[-2.5, -1.5,  3.5],
[ 0.5,  0.5,  0.5]]

nodes = []
for value in values:
    output = Percept([value[0], value[1]], -1 * value[2])
    nodes.append(output)
    
counter = 0

for a in nodes:
    first = copy.copy(a)
    for b in nodes:
        second = copy.copy(b)
        for c in nodes:
            third = copy.copy(c)
            first.set_inputs([x1,x2])
            second.set_inputs([x1,x2])
            third.set_inputs([first, second])
            xor = third
            # print(first.name, second.name, third.name)
            result = []
            for a in range(2):
                for b in range(2):
                    x1.set_value(a)
                    x2.set_value(b)
                    endEval = xor.evaluate()
                    result.append(endEval)
                    # print(a, b, endEval)
            # print(result)
            if result == target:
                counter += 1
            # print('\n')

print(counter)
"""




