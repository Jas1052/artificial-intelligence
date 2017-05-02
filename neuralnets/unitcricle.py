import numpy as np
import itertools
import copy
import math

#classes defined: Percept and Input(extends Percept)
#parameters: the weights (w_ij) and thresholds (t_j)

target = [0, 1, 1, 0]

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
print("done")
