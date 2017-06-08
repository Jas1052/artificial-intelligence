import numpy
import random

avals = [] ## list of a vals starting from matrix 1 column
ax = 'x/10'
aderiv = 1/10
epoch = 10

def back_prop(training_set):
    ##training_set: tuple of two lists. input, output
    inpu = training_set[0]
    output = training_set[1]
    ## while not stop condition:
        ## layer 1
    matrices = []
    
    matrix1 = []
    for i in range(len(inpu)):
        row = []
        for i in range(len(output)):
            row.append(random.uniform(-1, 1))
        matrix1.append(row)
    matrices.append(matrix1)
    matrix2 = []
    for i in range(len(output)):
        row = []
        for i in range(len(output)):
            row.append(random.uniform(-1, 1))
        matrix2.append(row)
    matrices.append(matrix2)

    for n in range(epoch):
        for sets in training_set:
            for matrix in matrices:
                for column_index in matrix[0]:
                    dot = 0
                    for row_index in range(len(matrix)): ## for each node j in layer L
                        weight = row[row_index]
                        total = weight*inpu[row_index]
                        dot += total
                    a.append(dot*aderiv)
                        
    print(matrix1)
    print(matrix2)

back_prop(([10,20,30],[2,1]))
