import copy
from queue import *

class node:
    def __init__(self, state, depth):
        self.state = state #2D array
        self.depth = depth
        #self.parent = parent
        self.children = []

# secondState is what nodeState is compared to
# returns false if they aren't identical, returns true otherwise

    def getState(self):
        return self.state

    def getDepth(self):
        return self.depth

    def getChildren(self):
        return self.children

    def compare(self, secondState):
        for y in range(0, 3):
            for x in range(0, 3):
                if self.state[y][x] != secondState[y][x]:
                    return False
        return True

    #checks if puzzle is solved
    def checkGoal(self):
        goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.compare(goalState)

    def findZero(self):
        for y in range(0, 3):
            for x in range(0, 3):
                if self.state[y][x] == 0:
                    return [y, x]

    def createChildren(self):
        zeroPos = self.findZero()  # y, x
        y = zeroPos[0]
        x = zeroPos[1]
        # moving 0 top; moving top piece into empty
        if y-1 > -1:
            temp = copy.deepcopy(self.state)    #copy state
            temp[y][x] = copy.deepcopy(temp[y-1][x])
            temp[y-1][x] = 0
            tempPuzzle = node(temp, self.depth + 1)
            self.children.append(tempPuzzle)
            # self.printState(temp)
         # moving 0 down; moving down piece into empty
        if y+1 < 3:
            temp = copy.deepcopy(self.state)
            temp[y][x] = copy.deepcopy(temp[y+1][x])
            temp[y+1][x] = 0
            tempPuzzle = node(temp, self.depth + 1)
            self.children.append(tempPuzzle)
            # self.printState(temp)
        # moving 0 left; moving left piece into empty
        if x-1 > -1:
            temp = copy.deepcopy(self.state)
            temp[y][x] = copy.deepcopy(temp[y][x-1])
            temp[y][x-1] = 0
            tempPuzzle = node(temp, self.depth + 1)
            self.children.append(tempPuzzle)
            # self.printState(temp)
        # moving 0 right; moving right piece into empty
        if x+1 < 3:
            temp = copy.deepcopy(self.state)
            temp[y][x] = copy.deepcopy(temp[y][x+1])
            temp[y][x+1] = 0
            tempPuzzle = node(temp, self.depth + 1)
            self.children.append(tempPuzzle)
            # self.printState(temp)

    def printState(self):
        print(self.state[0])
        print(self.state[1])
        print(self.state[2])
        print("\n")

fringe = Queue()
blocked = []

def solve(tree):   # tree is a node
    fringe.put(tree)
    while fringe.empty() is not True:
        nodeTemp = fringe.get()
        matrixTemp = nodeTemp.getState()
        if nodeTemp.checkGoal() is True:
            print(matrixTemp)
            exit()
        nodeTemp.createChildren()
        for i in range(0, len(nodeTemp.getChildren())):
            newNode = nodeTemp.getChildren()[i]  # newNode is child
            if newNode not in fringe.queue and newNode not in blocked:
                # newNode.printState()
                blocked.append(newNode)
                fringe.put(newNode)

# main

# making starting matrix
# start = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
start = [[0, 4, 3],
         [7, 1, 6],
         [5, 2, 8]]

tree = node(start, 1)
solve(tree)

