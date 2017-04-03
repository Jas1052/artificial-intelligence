import numpy as np

# learning rate
lamb = 1
epoch = 15

def find_weight(training_set):
    w = np.array([0.5, 0.5, 0.5])
    for val in range(epoch):
        for x, fx in training_set:
            f = actuator(np.dot(x, w))
            w = w + (lamb*(fx - f))*x
    accuracy = 1 - (sum([abs(fx-actuator(np.dot(x, w))) for x, fx in training_set]))/len(training_set)
    return w, accuracy

def actuator(val):
    return 1 if val > 0 else 0

def andOperator(arr):
    return 1 if val == 0 for val in arr

# takes n (binary number)
def create_set(val):
    ts = []
    retur ts

training_set = [(np.array([0, 0, 1]), 0), (np.array([1, 0, 1]), 0), (np.array([0, 1, 1]), 0), (np.array([1, 1, 1]), 1)]
weight = find_weight(training_set)
print(weight)
