import math
import csv

def make_ds():
    ds = {}
    csvArr = []
    with open('tennis_tree.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # rotate through vals in first row
        for row in reader:
            csvArr.append(row[0].split(','))

    # rotates through vals in first row
    for i in range(len(csvArr[0])):
        choices = []
        # rotates through row and gets choice
        for row in csvArr:
            choices.append(row[i])
        ds.update({csvArr[0][i]:choices})

    # drops repeated question in choices
    for val in list(ds.values()):
        val.pop(0)

    for key, val in list(ds.values()):
        # question : [entropy, choices, array tuple of freq]
        pass
    
    return ds

def make_tree(ds, level):
    pass

def entropy(list):
    total = 0
    listSum = sum(list)
    for val in list:
        if val is 0:
            total += 0
        else:
            total += (val/listSum) * math.log2(val/listSum)
    return -1 *  total

def avg_entropy(list):
    total = 0
    listSum = 0
    # gets total values in list
    for arr in list:
        for val in arr:
            listSum += val
    for arr in list:
        arrSum = sum(arr)
        total += (arrSum/listSum) * entropy(arr)
    return total

# print(entropy([3,4,1]))
# print(entropy([9,5]))
# exampleList = [[9,5],[10,4], [9,5],[10,4]]
# print(avg_entropy(exampleList))
print(make_ds())
