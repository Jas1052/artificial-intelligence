import numpy as np

# learning rate
lamb = 0.1

def find_weight(training_set):
    
    for each epoch:
        for x, fx in training_set:
            a = 1
            f = a(np.dot(x, w))
            w = w + x(fx - f)lamb
    return 
