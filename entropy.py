import math

def entropy(list):
    total = 0
    listSum = sum(list)
    for val in list:
        if val is 0:
            total += 0
        else:
            total += (val/listSum) * math.log(val/listSum, 2)
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
print(entropy([9,5]))
exampleList = [[9,5],[10,4], [9,5],[10,4]]
print(avg_entropy(exampleList))
