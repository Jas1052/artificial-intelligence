import numpy as np
import itertools

# learning rate
lamb = 1
epoch = 500
n = 2

def find_weight(training_set):
    w = np.array([0.5]*(n+1))
    for val in range(epoch):
        for (x, fx) in training_set:
            f = actuator(np.dot(x, w))
            w = w + (lamb*(fx - f))*x
    accuracy = 1 - (sum([abs(fx-actuator(np.dot(x, w))) for (x, fx) in training_set]))/len(training_set)
    # print(w)
    return (w, accuracy)

def actuator(val):
    return 1 if val > 0 else 0

# takes n (binary number)
def create_set(val):
    ts = []
    binaries = ["".join(seq) for seq in itertools.product("01", repeat=val)]
    for index in range(2**(2**val)):
        row = []
            for binary in binaries:
            tempBin = [int(d) for d in binary]
            tempBin.append(1)
            tempBin = np.array(tempBin)
            bi = bin(index)[2:].zfill(2**n)
            row.append((tempBin, int(bi[binaries.index(binary)])))
        ts.append(row)
    return ts

arrTS = create_set(n)
"""
for ts in arrTS:
    print(ts)
"""
output = []
total = 0
correct = 0
for ts in arrTS:
    vector, accuracy = find_weight(ts)
    if accuracy == 1.0:
        print(vector)
        correct += 1
accuracy = correct/len(arrTS)
print(correct)
print(accuracy)
# training_set = [(np.array([0, 0, 1]), 0), (np.array([1, 0, 1]), 0), (np.array([0, 1, 1]), 0), (np.array([1, 1, 1]), 1)]
# weight = find_weight(training_set)
# print(weight)
