import numpy as np
import itertools

#classes defined: Percept and Input(extends Percept)
#parameters: the weights (w_ij) and thresholds (t_j)

class Percept:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
        self.percepts = None
    def set_inputs(self, percepts):
        self.percepts = percepts
    def actuator(self, val):
        return 1 if val > self.threshold else 0
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
    
w13 = -1
w23 = -1
w14 = 1
w24 = 1
w35 = 1
w45 = 1
w36 = -1
w46 = -1

t3 = -1.5
t4 = 0.5
t5 = 1.5
t6 = -0.5

x1 = Input()
x2 = Input()

node_3 = Percept([w13,w23],t3) # nand
node_4 = Percept([w14,w24],t4) # or
node_5 = Percept([w35,w45],t5) # and 
node_6 = Percept([w36,w46],t6) # nor

node_3.set_inputs([x1,x2])
node_4.set_inputs([x1,x2])
node_5.set_inputs([node_3, node_4])
xor = node_5

for a in range(2):
    for b in range(2):
        x1.set_value(a)
        x2.set_value(b)
        print(a, b, xor.evaluate())
