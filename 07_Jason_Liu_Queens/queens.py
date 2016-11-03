# DFS
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
        for i in range(len(self.state)):
            if self.state[i] is -1:
                return i

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
    count = 0
    goalcount = 0
    fringe = deque([])
    fringe.append(board)
    while(True):
        if len(fringe) is 0:
            print("Empty Fringe")
            return
        n = fringe.pop()
        goalcount = goalcount + 1
        if n.goal_test():
            print goalcount
            return
        column = n.get_next_unassigned_var()
        for val in n.choices[column]:
            count = count+1
            child = nQueens(copy.deepcopy(n.state), copy.deepcopy(n.choices), copy.deepcopy(n.n), n)
            child.assign(column, val)
            fringe.append(child)

# ----------------------------------------------------------------

for i in range(5,50,3):
    begin = time.time()
    print '\n'
    board = nQueens(n=i)
    dfs_search(board)
    end = time.time()

    timer = str(round(end - begin, 3))
    print timer

"""
/usr/bin/python2.7 "/home/jliu/Documents/Link to Senior/AI/Queens/queens.py"


5
[4, 2, 0, 3, 1]
11
0.001


8
[7, 3, 0, 2, 5, 1, 6, 4]
124
0.014


11
[10, 8, 6, 4, 2, 0, 9, 7, 5, 3, 1]
85
0.013


14
[13, 11, 9, 7, 2, 4, 1, 10, 0, 5, 12, 8, 6, 3]
1934
0.325


17
[16, 14, 12, 15, 9, 6, 2, 10, 1, 3, 0, 13, 11, 8, 5, 7, 4]
5449
1.112


20
[19, 17, 15, 18, 16, 7, 5, 8, 2, 0, 3, 11, 4, 1, 12, 10, 13, 6, 14, 9]
199686
55.855


23
[22, 20, 18, 21, 19, 14, 12, 10, 5, 3, 1, 4, 2, 13, 15, 17, 0, 16, 7, 11, 8, 6, 9]
25328
8.29


26
[25, 23, 21, 24, 22, 17, 15, 13, 11, 5, 3, 1, 6, 4, 2, 0, 16, 19, 10, 14, 18, 20, 8, 12, 7, 9]
398246
159.538


29

"""