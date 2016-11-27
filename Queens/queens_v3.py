# random random
import time
import math
import heapq
from collections import deque
import copy
import random
import random

class nQueens:
    def __init__(self, state=None, choices=None, n=None, parent=None):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the state predecessor in a search
        """

        if n is None:
            print "problem with n"
            self.n = 8
        else:
            self.n = n

        if state is None:
            self.state = []
            for i in range(self.n):
                self.state.append(-1)
        else:
            self.state = state

        if choices is None:
            self.choices = []
            sub = set([])
            for a in range(self.n):  # puts 0 through 7 inclusive into sub
                sub.add(a)
            for i in range(self.n):  # puts sub into choices
                self.choices.append(copy.copy(sub))
        else:
            self.choices = choices

        if parent is not None:
            self.parent = parent

    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propgates constraints and updates choices
        """
        self.state[var] = value
        for column in self.choices:
            column.difference_update([value])  # removes row
        self.choices[var] = set([])  # removes column

        for xindex in range(len(self.choices)):              # iterate through sets in choice
            column = self.choices[xindex]                       # naming the set as column
            tempcol = copy.copy(column)
            for y in tempcol:                             # iterate through available rows in column
                if abs(y - value) == abs(xindex - var):    # check in y,x is a diagonal
                    column.difference_update([y])          # remove row val in column set

    def goal_test(self):
        """ returns True iff state is the goal state """
        if -1 in self.state:
            return False
        else:
            return True

    def get_next_unassigned_var(self):
        """ Returns the index of a column that is unassigned and
            has valid choices available """
        """
        i = 0
        mid = self.n//2
        if self.n%2 == 0:
            while mid - i > -1:
                randomVal = random.randint(0, self.n - 1)
                if self.state[randomVal] is -1:
                    return randomVal
        else:
            while mid + i < self.n:
                randomVal = random.randint(0, self.n - 1)
                if self.state[randomVal] is -1:
                    return randomVal"""

        while(True):
            randomVal = random.randint(0, self.n - 1)
            if self.state[randomVal] is -1:
                return randomVal

    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
             for variable var, possibly sorted """
        while(True):
            randomVal = random.randint(0, self.n - 1)
            if len(self.choices[randomVal]) != 0:
                return self.choices[randomVal]

    def __str__(self):
        """ returns a string representation of the object """
        return ''.join(str(e) + '  ' for e in self.state)

###---------------------------------------------------------------


def dfs_search(board):
    """ sets board as the initial state and returns a
        board containing an nQueens solution
        or None if none exists
    """
    goalcount = 0
    fringe = deque([])
    count = 0
    fringe.append(board)
    while(True):
        if len(fringe) is 0:
            print("Empty Fringe")
            return
        n = fringe.pop()
        # print(n)
        goalcount = goalcount + 1
        if n.goal_test():
            print goalcount
            print count
            return
        column = n.get_next_unassigned_var()
        tempcol = random.sample(n.choices[column], len(n.choices[column]))
        for val in tempcol:
            count = count+1
            child = nQueens(copy.deepcopy(n.state), copy.deepcopy(n.choices), copy.deepcopy(n.n), n)
            child.assign(column, val)
            fringe.append(child)
# ----------------------------------------------------------------

for i in range(5,100,3):
    begin = time.time()
    print '\n'
    print i
    board = nQueens(n=i)
    dfs_search(board)
    end = time.time()

    timer = str(round(end - begin, 3))
    print timer

"""
 /usr/bin/python2.7 "/home/jliu/Documents/Link to Senior/AI/Queens/queens_v3.py"


5
[0, 2, 4, 1, 3]
12
0.001


8
[4, 1, 3, 6, 2, 7, 5, 0]
29
0.004


11
[0, 4, 7, 1, 6, 2, 10, 8, 3, 5, 9]
190
0.031


14
[8, 5, 12, 0, 3, 10, 7, 13, 2, 9, 1, 6, 4, 11]
112
0.024


17
[10, 6, 11, 15, 12, 4, 0, 14, 9, 2, 5, 1, 8, 13, 16, 7, 3]
571
0.124


20
[2, 17, 6, 16, 12, 1, 3, 7, 13, 18, 5, 14, 10, 19, 15, 9, 4, 0, 8, 11]
508
0.141


23
[10, 12, 18, 16, 4, 7, 11, 21, 14, 2, 17, 15, 6, 3, 22, 0, 13, 8, 19, 5, 1, 20, 9]
602
0.197


26
[3, 11, 17, 7, 12, 25, 18, 13, 24, 22, 8, 10, 1, 4, 19, 0, 23, 5, 20, 9, 14, 21, 15, 6, 16, 2]
15440
4.767


29
[6, 1, 12, 8, 20, 24, 27, 14, 22, 10, 7, 15, 25, 3, 9, 17, 19, 5, 26, 28, 11, 4, 21, 16, 18, 23, 2, 0, 13]
3220
1.205


32
[21, 19, 26, 11, 8, 28, 3, 20, 15, 9, 25, 27, 7, 16, 10, 24, 30, 0, 29, 18, 22, 1, 12, 2, 6, 31, 17, 4, 13, 23, 14, 5]
7955
3.152


35
[3, 9, 4, 34, 18, 28, 23, 17, 32, 27, 16, 6, 1, 29, 11, 0, 2, 22, 25, 13, 8, 33, 12, 21, 24, 5, 30, 26, 10, 20, 31, 15, 19, 14, 7]
35551
17.354


38
[36, 20, 9, 0, 8, 11, 17, 10, 21, 26, 35, 33, 30, 27, 14, 16, 32, 29, 6, 24, 7, 5, 12, 31, 15, 34, 4, 37, 13, 23, 19, 2, 25, 28, 3, 18, 22, 1]
13726
7.799


41
[4, 21, 34, 40, 16, 24, 1, 38, 33, 5, 28, 20, 27, 36, 3, 13, 10, 30, 19, 0, 7, 12, 8, 25, 32, 15, 26, 37, 35, 22, 29, 11, 2, 39, 31, 18, 14, 9, 6, 23, 17]
3421
2.835


44
[26, 22, 38, 33, 13, 7, 5, 39, 30, 19, 6, 28, 40, 32, 21, 16, 41, 10, 15, 24, 4, 29, 3, 9, 37, 31, 42, 14, 2, 18, 25, 35, 43, 36, 0, 27, 8, 17, 20, 12, 23, 1, 11, 34]
2964
2.095


47
[34, 26, 18, 14, 1, 44, 24, 33, 4, 42, 19, 30, 35, 11, 7, 21, 23, 5, 28, 13, 6, 12, 46, 15, 32, 0, 2, 40, 17, 29, 20, 43, 37, 10, 3, 36, 8, 41, 16, 22, 39, 25, 45, 38, 9, 27, 31]
891
1.086


50
[11, 2, 18, 26, 32, 47, 37, 42, 4, 31, 12, 16, 21, 34, 44, 3, 29, 6, 10, 23, 35, 41, 22, 8, 15, 49, 43, 30, 7, 9, 40, 1, 14, 45, 48, 13, 20, 24, 28, 36, 46, 0, 17, 38, 27, 19, 39, 33, 25, 5]
11168
9.804


53
"""