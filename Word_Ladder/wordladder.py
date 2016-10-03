import copy
import heapq

import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class node:
    def __init__(self, word, parent, depth):
        self.word = word
        self.parent = parent
        self.depth = depth
        self.distance = self.calcDistance()

# secondState is what nodeState is compared to
# returns false if they aren't identical, returns true otherwise
    def __lt__(self, other):
        if self.distance < other.getDistance():
            return True
        else:
            return False

    def calcDistance(self):
        lettersWrong = 0
        for letter in self.word:
            pos = self.word.index(letter)
            if letter != goal[pos]:
                lettersWrong += 1
        return lettersWrong + self.depth

    def getDistance(self):
        return self.distance

    def getWord(self):
        return self.word

    def getParent(self):
        return self.parent

    #checks if puzzle is solved
    def checkGoal(self):
            if self.word == goal:
                return True

    def createChildren(self):
        tempWord = copy.deepcopy(self.word)
        for letter in self.word:
            pos = self.word.index(letter)
            for i in alphabet:
                newWord = tempWord[:pos] + i + tempWord[pos+1:]
                if newWord in wordList and newWord not in seen:
                    newChild = node(newWord, self, self.depth + 1)
                    heapq.heappush(fringe, newChild)
fringe = []
seen = set([])
count = []
solution = True

def solve(tree):
    heapq.heappush(fringe, tree)
    while len(fringe) is not 0:
        nodeTemp = heapq.heappop(fringe)
        seen.add(nodeTemp.getWord())
        if nodeTemp.checkGoal() is True:
            parentNode = nodeTemp
            while parentNode.getParent() is not None:
                count.append(parentNode.getWord())
                parentNode = parentNode.getParent()
            return
        nodeTemp.createChildren()
    solution = False
    return

# main
# using sets, no repetitions, "in mySet" is very fast,

words = [line.rstrip('\n') for line in open('dictionary.txt')]  # stores dictionary in lines list
wordList = set(words)

with open('puzzleB.txt') as f:
    puzzles = [line.rstrip('\n') for line in open('puzzleB.txt')]
    print(puzzles)
output = ''
for puzzle in puzzles:
    begin = time.time()
    puzzleWords = puzzle.split(' ')
    print(puzzleWords)
    start = puzzleWords[0]
    goal = puzzleWords[1]

    seen.add(start)
    tree = node(start, None, 1)

    solve(tree)

    num = str(len(count))
    if len(count) == 0:
        num = '--'
    end = time.time()
    timer = str(round(end - begin, 3))
    # print(start + " " + goal + " " + num + " " + timer)
    output = output + "\n" + start + " " + goal + " " + num + " " + timer

    seen.clear()
    fringe.clear()
    count.clear()

text_file = open("solutions.txt", "w")
text_file.write(output)
text_file.close()