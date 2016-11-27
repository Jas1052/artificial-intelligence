# random column
import time
import math
import heapq
from collections import deque
import copy
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
        while(True):
            randomVal = random.randint(0, self.n - 1)
            if self.state[randomVal] is -1:
                return randomVal

    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
             for variable var, possibly sorted """
        return self.choices[var]

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
        for val in n.choices[column]:
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
 /usr/bin/python2.7 "/home/jliu/Documents/Link to Senior/AI/Queens/queens_v2.py"


5
[3, 0, 2, 4, 1]
11
0.001


8
[6, 4, 2, 0, 5, 7, 1, 3]
35
0.007


11
[7, 0, 4, 6, 9, 3, 10, 8, 2, 5, 1]
111
0.039


14
[7, 4, 10, 3, 13, 6, 2, 9, 12, 1, 5, 8, 11, 0]
78
0.031


17
[4, 9, 13, 6, 1, 3, 11, 7, 15, 10, 16, 2, 0, 5, 8, 14, 12]
755
0.278


20
[4, 11, 0, 2, 16, 14, 19, 15, 10, 5, 13, 6, 3, 18, 7, 1, 17, 9, 12, 8]
218
0.067


23
[21, 15, 6, 8, 3, 12, 0, 5, 17, 20, 10, 13, 1, 9, 4, 18, 22, 2, 19, 16, 11, 7, 14]
215
0.106


26
[13, 20, 8, 19, 4, 14, 10, 17, 23, 11, 2, 22, 5, 25, 9, 0, 12, 1, 16, 7, 21, 24, 3, 6, 18, 15]
688
0.284


29
[13, 16, 26, 24, 20, 2, 9, 5, 14, 0, 27, 21, 11, 1, 4, 15, 23, 18, 22, 28, 25, 10, 7, 3, 17, 8, 12, 19, 6]
336
0.228


32
[5, 19, 9, 29, 17, 24, 18, 21, 23, 7, 16, 27, 15, 4, 31, 8, 3, 26, 0, 11, 30, 1, 12, 2, 25, 22, 28, 10, 13, 6, 14, 20]
2505
1.82


35
[32, 19, 21, 16, 26, 9, 34, 3, 29, 8, 33, 31, 10, 18, 11, 6, 17, 24, 20, 25, 28, 15, 7, 1, 27, 2, 13, 22, 0, 5, 30, 4, 14, 12, 23]
32534
18.458


38
[16, 31, 23, 15, 22, 0, 3, 13, 7, 26, 2, 37, 19, 17, 5, 24, 21, 36, 4, 30, 14, 6, 1, 33, 27, 8, 34, 9, 29, 18, 20, 12, 32, 35, 11, 28, 10, 25]
4222
2.151


41
[36, 21, 1, 4, 19, 39, 33, 28, 3, 12, 22, 20, 26, 30, 27, 38, 32, 7, 10, 0, 13, 5, 24, 34, 6, 2, 11, 18, 14, 35, 37, 9, 40, 29, 31, 23, 15, 17, 25, 8, 16]
5752
3.246


44
[12, 35, 29, 6, 11, 28, 1, 43, 22, 5, 19, 10, 27, 21, 38, 8, 32, 34, 36, 13, 0, 40, 20, 23, 25, 30, 14, 33, 7, 15, 41, 16, 24, 4, 9, 3, 17, 39, 42, 26, 37, 18, 31, 2]
1749
2.241


47
[12, 29, 18, 37, 34, 10, 3, 30, 25, 44, 31, 35, 14, 5, 22, 24, 41, 28, 32, 39, 8, 43, 20, 0, 19, 7, 36, 21, 27, 2, 4, 38, 17, 33, 1, 16, 11, 40, 6, 45, 23, 42, 46, 13, 15, 9, 26]
11170
9.816


50

"""