import copy

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
                    print("false")
                    return False
        print("true")
        return True

    #checks if puzzle is solved
    def checkGoal(self):
        goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.printState(goalState)
        self.compare(goalState)

    def findZero(self):
        for y in range(0, 3):
            for x in range(0, 3):
                if self.state[y][x] == 0:
                    return [y, x]

    def createChildren(self):
        zeroPos = self.findZero()  # y, x
        y = zeroPos[0]
        x = zeroPos[1]
        self.printState(self.state)
        # moving 0 top; moving top piece into empty
        if y-1 > -1:
            temp = copy.deepcopy(self.state)    #copy state
            temp[y][x] = copy.deepcopy(temp[y-1][x])
            temp[y-1][x] = 0
            self.children.append(temp)
            # self.printState(temp)
         # moving 0 down; moving down piece into empty
        if y+1 < 3:
            temp = copy.deepcopy(self.state)
            temp[y][x] = copy.deepcopy(temp[y+1][x])
            temp[y+1][x] = 0
            self.children.append(temp)
            # self.printState(temp)
        # moving 0 left; moving left piece into empty
        if x-1 > -1:
            temp = copy.deepcopy(self.state)
            temp[y][x] = copy.deepcopy(temp[y][x-1])
            temp[y][x-1] = 0
            self.children.append(temp)
            # self.printState(temp)
        # moving 0 right; moving right piece into empty
        if x+1 < 3:
            temp = copy.deepcopy(self.state)
            temp[y][x] = copy.deepcopy(temp[y][x+1])
            temp[y][x+1] = 0
            self.children.append(temp)
            # self.printState(temp)

    def printState(self, matrix):
        print(matrix[0])
        print(matrix[1])
        print(matrix[2])
        print("\n")

def solve(tree):
    print(tree.printState(tree.getState()))
    tree.createChildren()


# main

# making starting matrix
start = [[4, 3, 2], [6, 0, 5], [8, 7, 1]]

tree = node(start, 1)
solve(tree)

