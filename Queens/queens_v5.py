# Name: Jason Liu
#  Block: 7
#  Email: 2017jliu@tjhsst.edu


import time
import math
import heapq
from collections import deque
import copy
import random
from random import shuffle

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

        """ pos:updated position of constrained column
            newpos: current position of column
            shortest: shortest set/coluumn
            newshortest: current length ohf set/column
        """

        pos = 0
        shortest = self.n
        for i in range(len(self.choices)):
            newpos = i
            newshortest = len(self.choices[i])
            if newshortest < shortest and newshortest != 0:
                shortest = newshortest
                pos = newpos
        return pos



    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
             for variable var, possibly sorted """
        """ unused"""
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
    count = 0
    goalcount = 0
    fringe = deque([])
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
        """Reversing Row"""
        ar = []
        for val in n.choices[column]:
            ar.append(val)
        ar.reverse()
        for val in ar:
            count = count + 1
            child = nQueens(copy.deepcopy(n.state), copy.deepcopy(n.choices), copy.deepcopy(n.n), n)
            child.assign(column, val)
            fringe.append(child)
# ----------------------------------------------------------------
"""looping from 5 to 150 for n"""
for i in range(5,150,3):
    begin = time.time()
    print '\n'
    print i
    board = nQueens(n=i)
    dfs_search(board)
    end = time.time()

    timer = str(round(end - begin, 3))
    print timer

"""
/usr/bin/python2.7 "/home/jliu/Documents/Link to Senior/AI/Queens/queens_v5.py"


5
[0, 2, 4, 1, 3]
11
0.001


8
[0, 4, 7, 5, 2, 6, 1, 3]
119
0.014


11
[0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
148
0.028


14
[0, 2, 4, 11, 8, 3, 12, 10, 13, 6, 1, 5, 7, 9]
299
0.061


17
[0, 2, 4, 13, 10, 3, 9, 6, 16, 14, 1, 15, 5, 8, 11, 7, 12]
168
0.043


20
[0, 2, 4, 13, 16, 3, 15, 6, 11, 17, 14, 18, 5, 9, 19, 10, 7, 1, 12, 8]
217
0.065


23
[0, 2, 4, 16, 12, 3, 22, 6, 13, 18, 14, 21, 5, 20, 17, 10, 7, 1, 8, 11, 9, 15, 19]
861
0.262


26
[0, 2, 4, 17, 11, 3, 21, 6, 18, 13, 15, 20, 5, 19, 25, 23, 7, 12, 1, 9, 14, 24, 8, 10, 16, 22]
524
0.31


29
[0, 2, 4, 23, 21, 3, 22, 6, 26, 15, 17, 20, 5, 16, 19, 25, 7, 28, 1, 27, 24, 11, 8, 12, 18, 13, 10, 14, 9]
382
0.211


32
[0, 2, 4, 25, 17, 3, 21, 6, 26, 13, 22, 31, 5, 23, 11, 18, 7, 24, 27, 30, 28, 10, 8, 29, 16, 1, 20, 12, 15, 9, 14, 19]
351
0.259


35
[0, 2, 4, 24, 22, 3, 16, 6, 30, 20, 25, 28, 5, 18, 27, 19, 7, 31, 34, 13, 26, 33, 8, 10, 12, 15, 21, 1, 9, 32, 14, 11, 17, 29, 23]
3993
1.836


38
[0, 2, 4, 26, 29, 3, 28, 6, 17, 13, 36, 30, 5, 24, 34, 25, 7, 33, 14, 16, 23, 10, 8, 35, 37, 32, 18, 1, 11, 9, 12, 21, 27, 20, 22, 19, 15, 31]
556
0.46


41
[0, 2, 4, 15, 27, 3, 22, 6, 12, 20, 31, 24, 5, 30, 23, 29, 7, 37, 40, 14, 39, 11, 8, 33, 16, 32, 1, 35, 25, 9, 36, 34, 17, 38, 18, 13, 19, 10, 26, 28, 21]
523
0.645


44
[0, 2, 4, 26, 24, 3, 30, 6, 16, 40, 15, 29, 5, 28, 25, 22, 7, 14, 39, 31, 42, 11, 8, 36, 27, 35, 43, 41, 37, 9, 34, 12, 38, 20, 1, 23, 19, 10, 33, 17, 32, 13, 21, 18]
1401
1.282


47
[0, 2, 4, 26, 21, 3, 20, 6, 28, 19, 25, 29, 5, 24, 42, 27, 7, 44, 39, 41, 14, 11, 8, 36, 43, 33, 15, 23, 37, 9, 34, 12, 16, 30, 40, 38, 18, 10, 45, 31, 35, 46, 13, 1, 32, 17, 22]
1847
1.567


50
[0, 2, 4, 30, 25, 3, 22, 6, 27, 43, 21, 31, 5, 42, 45, 24, 7, 34, 23, 37, 26, 13, 8, 46, 20, 47, 38, 35, 17, 9, 44, 12, 36, 40, 49, 1, 39, 10, 48, 14, 18, 29, 19, 33, 41, 15, 11, 16, 32, 28]
1000
1.417


53
[0, 2, 4, 26, 23, 3, 27, 6, 47, 44, 30, 49, 5, 22, 31, 52, 7, 25, 21, 24, 46, 13, 8, 29, 40, 37, 39, 45, 50, 9, 41, 38, 14, 43, 48, 1, 51, 10, 42, 36, 18, 15, 17, 20, 33, 28, 11, 32, 35, 12, 34, 19, 16]
2467
2.326


56
[0, 2, 4, 52, 31, 3, 53, 6, 23, 30, 43, 29, 5, 51, 42, 27, 7, 26, 47, 25, 50, 13, 8, 40, 38, 48, 34, 22, 41, 9, 49, 21, 54, 18, 44, 1, 39, 10, 16, 55, 45, 17, 46, 37, 28, 32, 11, 35, 20, 12, 24, 15, 19, 14, 33, 36]
1631
2.34


59
[0, 2, 4, 25, 31, 3, 30, 6, 51, 53, 57, 37, 5, 58, 26, 19, 7, 38, 35, 27, 34, 55, 8, 28, 56, 36, 44, 33, 22, 9, 15, 50, 47, 49, 29, 42, 13, 10, 20, 48, 43, 54, 52, 1, 40, 21, 11, 17, 45, 16, 24, 39, 23, 32, 18, 14, 12, 46, 41]
1304
2.483


62
[0, 2, 4, 50, 31, 3, 39, 6, 40, 60, 41, 45, 5, 28, 52, 24, 7, 38, 22, 42, 34, 57, 8, 36, 61, 37, 46, 33, 35, 9, 20, 27, 54, 49, 59, 32, 13, 10, 56, 58, 48, 51, 29, 1, 55, 30, 11, 17, 43, 16, 53, 19, 44, 47, 25, 21, 12, 26, 15, 18, 14, 23]
3681
5.346


65
[0, 2, 4, 39, 25, 3, 50, 6, 61, 46, 41, 54, 5, 35, 38, 31, 7, 43, 60, 34, 23, 33, 8, 36, 59, 42, 32, 37, 62, 9, 20, 56, 29, 53, 28, 44, 13, 10, 57, 27, 63, 55, 47, 1, 19, 26, 11, 51, 24, 45, 58, 40, 30, 48, 16, 21, 12, 64, 15, 18, 52, 14, 22, 17, 49]
2789
4.807


68

"""