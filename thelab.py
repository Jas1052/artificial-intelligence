import time
import math
import heapq
from collections import deque
import random
import copy


class nQueens:
    def __init__(self, state=None, choices=None, n=None, parent=None):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the state predecessor in a search
        """
        if n is None:
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
            st = set([])
            for i in range(self.n):
                st.add(i)
            for j in range(self.n):
                self.choices.append(copy.copy(st))
        else:
            self.choices = choices

        self.parent = parent

    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propagates constraints and updates choices
            var is the column number
            value is the position in the column(row number)
        """
        self.state[var] = value
        for column in self.choices:
            column.discard(value)
        self.choices[var] = set([])

        for i in range(len(self.choices)):  # go through all the columns
            col = self.choices[i]  # pick a column
            copycol = copy.copy(col)
            for j in copycol:  # go through all the rows
                if abs( - var) == abs(j - value):  # if the "slope" is one
                    col.discard(j)  # get em outta there

        print(self.choices)

    def goal_test(self):
        """ returns True iff state is the goal state """
        # print(self.state)
        if -1 in self.state:  # simple enough, if the state still has empty columns, return False
            return False
        else:
            print("reached goal")
            return True

    def get_next_unassigned_var(self):
        """ returns the index of a column that is unassigned and
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
        out = ""
        for i in range(len(self.state)):
            out = out + '\n'
            for j in range(8):
                if self.state[j] == -1:
                    out = out + " " + "-1"
                else:
                    out = out + ' ' + 'Q'
        return out


# ##---------------------------------------------------------------

def dfs_search(queen):
    """ sets board as the initial state and returns a
        board containing an nQueens solution
        or None if none exists
    """
    fringe = deque([queen])
    while True:
        if len(fringe) is 0:
            return "Fringe is empty :("
        n = fringe.pop()
        if n.goal_test():
            print("reached goal")
            return n
        col = n.get_next_unassigned_var()
        for val in n.choices[col]:
            c = nQueens(copy.deepcopy(n.state), copy.deepcopy(n.choices), copy.deepcopy(n.n), n)
            c.assign(col, val)
            fringe.append(c)
    print 'end'


# ##---------------------------------------------------------------

board = nQueens()
dfs_search(board)



