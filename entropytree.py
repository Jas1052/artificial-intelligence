import math
import csv
import copy

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

def make_ds():
    ds = {}
    csvArr = []
    with open(csvName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # rotate through vals in first row
        for row in reader:
            csvArr.append(row)
    # rotates through vals in first row
    for i in range(len(csvArr[0])):
        choices = []
        # rotates through row and gets choice
        for row in csvArr:
            choices.append(row[i])
        ds[csvArr[0][i]] = choices
    
    # drops repeated question in choices
    """
    for val in list(ds.values()):
        print(val[0])
        val.pop(0)
    """
    global answers
    global label
    ds.pop(label, None)
    return ds

def make_tree(ds, level):
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
        # print(str(key) + ': ' + str(avg_entropy(yesno)))
        if avg_entropy(yesno) < lowest_entropy:
            best_col_key = key
            lowest_entropy = avg_entropy(yesno)
    # print('best key: ' + str(best_col_key))
    ds[bigQuestion] = answers
    print("---" * level, best_col_key, "?")
    # print('Best Col Key: ' + best_col_key)
    best_col = list(set(ds[best_col_key]))
    for val in best_col:
        new_ds = extract(ds, best_col_key, val)
        if isEntropyZero(new_ds):
            print('---' * level + "> ", str(val), new_ds[bigQuestion][0])
        else:
            print('---' * level + "> " + str(val) + "...")
            make_tree(new_ds, level + 1)

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

data_structure = make_ds()
# print(data_structure)
make_tree(data_structure, 0)
