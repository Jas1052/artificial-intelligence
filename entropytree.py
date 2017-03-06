import math
import csv
import copy

answers = []
full_table = {}

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

    global answers
    answers = ds['Play?']
    ds.pop('Day', None)
    global full_table
    full_table = copy.copy(ds)
    ds.pop('Play?', None)

    for key, val in ds.items():
        # question : [entropy, array of choices, array of array of yesno]
        choices = []
        yesno = []
        for i in range(len(val)):
            option = val[i]
            if option in choices:
                if answers[i] == 'Yes':
                    yesno[choices.index(option)][0] += 1
                else:
                    yesno[choices.index(option)][1] += 1
            else:
                choices.append(option)
                yesno.append([0, 0])
                if answers[i] == 'Yes':  # cannot use 'is'
                    yesno[choices.index(option)][0] += 1
                else:
                    yesno[choices.index(option)][1] += 1
        """
        for i in range(len(choices)):
            freq.append(0)
        for option in val:
            freq[choices.index(option)] += 1
        """
        ds[key] = [avg_entropy(yesno), choices, yesno]
    return ds

# question : [entropy, array of choices, array of array of yesno]
def make_tree(ds, level, table):
    if level is 10:
        exit(0)
    best_col_key = None
    lowest_entropy = 999
    for key, val in ds.items():
        if val[0] < lowest_entropy:
            best_col_key = key
            lowest_entropy = val[0]
    best_col = ds[best_col_key][1]
    print("---" * level, best_col_key, "?")
    for val in best_col:
        new_ds, new_table = extract(ds, best_col, best_col_key, val, table)
        if isSame(new_ds):
            print('---' * level + "> ", str(val), getAnswer(new_ds))
        else:
            print('---' * level + "> " + str(val) + "...")
            make_tree(new_ds, level + 1, new_table)

def isSame(ds):
    for key, val in ds.items():
        if val == []:
            return True
        if val[0] != 0.0:
            return False
    return True

def getAnswer(ds):
    for val in ds.values():
        if val[2][0][1] is not 0:
            return 'Yes'
    else:
        return 'No'

def extract(ds, best_col, best_col_key, val, table):
    indices = []
    for i in range(len(table[best_col_key])):
        if table[best_col_key][i] == val:
            indices.append(i)
    new_ds = {}
    # question : [entropy, array of choices, array of array of yesno]
    for key, value in table.items():
        questionValues = []
        for i in indices:
            questionValues.append(value[i])
        new_ds[key] = questionValues
    new_ds.pop(best_col_key, None)
    answers = new_ds['Play?']
    new_ds.pop('Play?', None)
    for key, value in new_ds.items():
        choices = []
        yesno = []
        for i in range(len(value)):
            option = value[i]
            if option in choices:
                if answers[i] == 'Yes':
                    yesno[choices.index(option)][0] += 1
                else:
                    yesno[choices.index(option)][1] += 1
            else:
                choices.append(option)
                yesno.append([0, 0])
                if answers[i] == 'Yes':  # cannot use 'is'
                    yesno[choices.index(option)][0] += 1
                else:
                    yesno[choices.index(option)][1] += 1
            new_ds[key] = [avg_entropy(yesno), choices, yesno]
    new_table = copy.copy(table)
    for key, value in new_table.items():
        newVal = []
        for i in range(len(value)):
            if i not in indices:
                newVal.append(value[i])
        new_table[key] = newVal
    new_table.pop(best_col_key, None)
    return new_ds, new_table

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
data_structure = make_ds()
print(data_structure)
make_tree(data_structure, 0, full_table)
