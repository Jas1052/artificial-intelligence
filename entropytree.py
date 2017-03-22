import math
import csv
import copy
import random

"""
csvName = 'tennis_tree.csv'
label = 'Day'
bigQuestion = 'Play?'
answerOne = 'Yes'
answerTwo = 'No'
"""
"""
csvName = 'cook.csv'
label = 'Label'
bigQuestion = 'EatOut?'
answerOne = 'GoOUT'
answerTwo = 'EatIN'
"""
csvName = 'house-votes-84.csv'
label = 'Label'
bigQuestion = 'Party?'
answerOne = 'republican'
answerTwo = 'democrat'

leftoverRows = []

class Node(object):
    "Generic tree node."
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def print(self, level=1):
        print(self.value)
        if self.children is not []:
            for child in self.children:
                for i in range(level):
                    print('----', end='')
                print(' ', end='')
                child.print(level+1)

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

def make_ds(numberOfRows):
    ds = {}
    csvArr = []
    with open(csvName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # rotate through vals in first row
        [csvArr.append(row) for row in reader]
    csvArr = randRows(csvArr, numberOfRows)
    # rotates through vals in first row
    for i in range(len(csvArr[0])):
        choices = []
        # rotates through row and gets choice
        for row in csvArr:
            # checks for missing data (?)
            if '?' not in row:
                choices.append(row[i])
        ds[csvArr[0][i]] = choices
    # drops repeated question in choices
    [val.pop(0) for val in list(ds.values())]
    global answers
    global label
    ds.pop(label, None)
    return ds

def make_tree(ds, level, node):
    global bigQuestion
    global answerOne
    best_col_key = None
    lowest_entropy = 999
    answers = ds.pop(bigQuestion, None)
    for key, val in ds.items():
        # checks for lowest entropy
        choices = []
        yesno = []
        for i in range(len(val)):
            option = val[i]
            if option in choices:
                if answers[i] == answerOne:
                    yesno[choices.index(option)][0] += 1
                else:
                    yesno[choices.index(option)][1] += 1
            else:
                choices.append(option)
                yesno.append([0, 0])
                if answers[i] == answerOne:  # cannot use 'is'
                    yesno[choices.index(option)][0] += 1
                else:
                    yesno[choices.index(option)][1] += 1
        if avg_entropy(yesno) < lowest_entropy:
            best_col_key = key
            lowest_entropy = avg_entropy(yesno)
    ds[bigQuestion] = answers
    # print("---" * level, best_col_key, "?")
    best_col = list(set(ds[best_col_key]))
    for val in best_col:
        new_ds = extract(ds, best_col_key, val)
        if isEntropyZero(new_ds):
            new_child = Node((best_col_key, val))
            new_child.add_child(Node((new_ds[bigQuestion][0], None)))
            node.add_child(new_child)
            # print('---' * level + "> ", str(val), new_ds[bigQuestion][0])
        else:
            # print('---' * level + "> " + str(val) + "...")
            new_child = Node((best_col_key, val))
            node.add_child(new_child)
            make_tree(new_ds, level + 1, new_child)
            
def randRows(arr, number):
    blocked = []
    number = len(arr)-number
    global leftoverRows
    leftoverRows.append(arr[0])
    for val in range(number):
        randomIndex = random.randint(1, len(arr) - 1)
        blocked.append(randomIndex)
        removed = arr.pop(randomIndex)
        leftoverRows.append(removed)
    return arr

def isEntropyZero(ds):
    global bigQuestion
    test = ds[bigQuestion][0]
    for value in ds[bigQuestion]:
        if value != test:
            return False
    return True

def extract(ds, best_col_key, val):
    new_ds = copy.copy(ds)
    indices = []
    for i in range(len(ds[best_col_key])):
        choice = new_ds[best_col_key][i]
        if choice == val:
            indices.append(i)
    # print(indices)
    for key, val in new_ds.items():
        new_arr = []
        for i in range(len(val)):
            if i in indices:
                new_arr.append(val[i])
        new_ds[key] = new_arr
    new_ds.pop(best_col_key, None)
    return new_ds

def freq_entropy(freq):
    s = sum(freq)
    p = [i /s for i in freq]
    return (-sum([i*math.log(i,2) for i in p if i>0]))

"""
def entropy(list):
    total = 0
    listSum = sum(list)
    for val in list:
        if val is 0:
            total += 0
        else:
            total += (val/listSum) * math.log2(val/listSum)
    return -1 *  total
"""

def avg_entropy(list):
    total = 0
    listSum = 0
    # gets total values in list
    for arr in list:
        for val in arr:
            listSum += val
    for arr in list:
        arrSum = sum(arr)
        total += (arrSum/listSum) * freq_entropy(arr)
    return total

def convert_to_ds(arr):
    ds = {}
    for i in range(len(arr[0])):
        choices = []
        # rotates through row and gets choice
        for row in arr:
            # checks for missing data (?)
            if '?' not in row:
                choices.append(row[i])
        ds[arr[0][i]] = choices
    # drops repeated question in choices
    for val in list(ds.values()):
        val.pop(0)
    global label
    ds.pop(label, None)
    return ds

def test_accuracy(tree, ds):
    correct = 0
    length = len(ds[bigQuestion])
    for i in range(length):
        currentNode = tree
        answerFound = False
        unknown = False
        while currentNode.get_children() != []:
            #print(currentNode.print())
            for child in currentNode.get_children():
                if child.get_value()[0] == answerOne or child.get_value()[0] == answerTwo:
                    currentNode = child
                    answerFound = True
                if answerFound is False and child.get_value()[1] == ds[child.get_value()[0]][i]:
                    currentNode = child
        if currentNode.get_value()[0] == ds[bigQuestion][i] and unknown == False:
            correct += 1
    return correct/length

for i in range(15, 200, 5):
    total = 0
    for trial in range(10):
        root = Node(('root', None))
        rows = i
        data_structure = make_ds(rows)
        # print(data_structure)
        make_tree(data_structure, 0, root)
        # root.print()
        leftoverDS = convert_to_ds(leftoverRows)
        accuracy = test_accuracy(root, leftoverDS)
        total += accuracy
        #print(str(accuracy))
        leftoverRows = []
    print(total/10)
