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
            print("problem with n")
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
            print(n)
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
i = 9
begin = time.time()
board = nQueens(n=i)
dfs_search(board)
end = time.time()
timer = str(round(end - begin, 3))
print(timer)

