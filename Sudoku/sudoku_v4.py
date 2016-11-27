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
        self.board =    [ [8, 0, 0,  0, 0, 0,  0, 0, 0],
                          [0, 0, 3,  6, 0, 0,  0, 0, 0],
                          [0, 7, 0,  0, 9, 0,  2, 0, 0],

                          [0, 5, 0,  0, 0, 7,  0, 0, 0],
                          [0, 0, 0,  0, 4, 5,  7, 0, 0],
                          [0, 0, 0,  1, 0, 0,  0, 3, 0],

                          [0, 0, 1,  0, 0, 0,  0, 6, 8],
                          [0, 0, 8,  5, 0, 0,  0, 1, 0],
                          [0, 9, 0,  0, 0, 0,  4, 0, 0]]

        if n is None:
            print("problem with n")
            self.n = 8
        else:
            self.n = n

        if state is None:
            self.state = []
            for i in range(self.n):
                self.state.append([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        else:
            self.state = state

        if choices is None:
            self.choices = []
            temp = []
            sub = set([])
            for a in range(self.n):  # puts 0 through 7 inclusive into sub
                sub.add(a)
            for i in range(self.n):  # puts sub into choices
                temp.append(copy.deepcopy(sub))
            for j in range(self.n):
                self.choices.append(copy.deepcopy(temp))
        else:
            self.choices = choices

        if parent is not None:
            self.parent = parent

    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propgates constraints and updates choices
        """
        self.state[keyValue][var] = value
        for column in self.choices[keyValue]:
            column.discard(value)  # removes row
        self.choices[keyValue][var] = set([])  # removes column
        for i in self.choices: # i is 1 whole board of choices
            i[var].discard(value)

        """for xindex in range(len(self.choices[keyValue])):              # iterate through sets in choice
            column = self.choices[keyValue][xindex]                       # naming the set as column
            tempcol = copy.copy(column)
            for y in tempcol:                             # iterate through available rows in column
                if abs(y - value) == abs(xindex - var):    # check in y,x is a diagonal
                    column.discard(y)          # remove row val in column set
        """

    def goal_test(self):
        """ returns True iff state is the goal state """
        collect = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for i in range(len(self.state)):
            xIndex = i
            yIndex = self.state[keyValue][i]
            bigX = xIndex // 3
            bigY = yIndex // 3
            while (bigX, bigY) in collect:
                collect.remove((bigX, bigY))

        if len(collect) == 0:
            return True
        else:
            return False

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
        for i in range(len(self.choices[keyValue])):
            newpos = i
            newshortest = len(self.choices[keyValue][i])
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
            if len(self.choices[keyValue][randomVal]) != 0:
                return self.choices[keyValue][randomVal]


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
            #print(n)
            return n
        column = n.get_next_unassigned_var()
        """Reversing Row"""
        ar = []
        for val in n.choices[keyValue][column]:
            ar.append(val)
        ar.reverse()
        for val in ar:
            count = count + 1
            child = nQueens(copy.deepcopy(n.state), copy.deepcopy(n.choices), copy.deepcopy(n.n), n)
            child.assign(column, val)
            """put square parameter below"""
            fringe.append(child)
# ----------------------------------------------------------------
"""looping from 5 to 150 for n"""
i = 9
keyValue = 0
begin = time.time()
board = nQueens(n=i)

output = dfs_search(board)

print(output.state)
print(output.choices)