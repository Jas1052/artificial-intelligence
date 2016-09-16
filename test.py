import copy
test = [[1,2,3],[1,2,3],[1,2,3]]
temp = copy.deepcopy(test)
temp[0][0] = 5
print(test)
print(temp)