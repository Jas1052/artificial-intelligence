from math import pi , acos , sin , cos
import time
import heapq

class cityNode:
    def __init__(self, cityCode, dist):
        self.cityCode = cityCode
        self.distanceFromStart = float(dist)
        self.children = []
        self.toGoal = calcd(coordinates[cityCode][0], coordinates[cityCode][1], goalCoord[0], goalCoord[1])

    def __lt__(self, other):
        f1 = self.toGoal + self.distanceFromStart
        f2 = other.getToGoal() + other.getDist()
        if f1 < f2:
            return True
        else:
            return False

    def getToGoal(self):
        return self.toGoal

    def getCity(self):
        return self.cityCode

    def getChildren(self):
        return self.children

    def getDist(self):
        return self.distanceFromStart

    def createChildren(self):
        childrenDict = railroads[self.cityCode]
        childrenList = [(k, v) for k, v in childrenDict.items()]
        childrenNodes = []
        for child in childrenList:
            childNode = cityNode(child[0], str(child[1] + float(self.distanceFromStart)))
            if childNode.getCity() not in seen:
                childrenNodes.append(childNode)
                seen.add(childNode.getCity())
        self.children = childrenNodes

    def __str__(self):
        return str(self.getCity()) + " : " + str(self.getDist())

def calcd(y1,x1, y2,x2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   return acos(min(1, sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1))) * R

# main
latlong = [line.rstrip('\n') for line in open('rrNodes.txt')]
coordinates = {}
for coordinate in latlong:
    info = coordinate.split(' ')
    coordinates[info[0]] = (info[1], info[2])
edges = [line.rstrip('\n') for line in open('rrEdges.txt')]
railroads = {}
for edge in edges:
    info = edge.split(' ')
    distance = calcd(coordinates[info[0]][0], coordinates[info[0]][1], coordinates[info[1]][0], coordinates[info[1]][1])
    if info[0] not in railroads:
        railroads[info[0]] = {info[1]: distance}
    else:
        railroads[info[0]].update({info[1]: distance})
    if info[1] not in railroads:
        railroads[info[1]] = {info[0]: distance}
    else:
        railroads[info[1]].update({info[0]: distance})

cities = [line.rstrip('\n') for line in open('rrCities.txt')]
cityCodes = {}
for city in cities:
    info = city.split(' ', 1)
    cityCodes.update({info[1]: info[0]})

fringe = []
seen = set([])
output = ''

def solve(tree):
    heapq.heappush(fringe, tree)
    while len(fringe) is not 0:
        nodeTemp = heapq.heappop(fringe)
        if nodeTemp.getCity() == goal:
            print("Distance: " + str(format(nodeTemp.getDist(), '.2f')))
            return str(format(nodeTemp.getDist(), '.2f'))
        nodeTemp.createChildren()
        for child in nodeTemp.getChildren():
            heapq.heappush(fringe, child)
        nodeTemp.createChildren()
    print("ran out")
    return

with open('test.txt') as f:
    tests = [line.rstrip('\n') for line in open('test.txt')]

for test in tests:
    begin = time.time()

    fromTo = test.split(', ')
    goal = cityCodes[fromTo[1]]
    goalCoord = coordinates[goal]
    startCode = cityCodes[fromTo[0]]
    starter = cityNode(startCode, 0)
    distanceTraveled = solve(starter)

    end = time.time()
    timer = str(round(end - begin, 3))
    #output = output + fromTo[0] + fromTo[1] + " " + distanceTraveled + " " + timer + '\n'
    output = output + '{:15s} {:15s} {:15s} {:15s}'.format(fromTo[0], fromTo[1], distanceTraveled, timer) + '\n'

    totalDistance = ''
    seen.clear()
    fringe.clear()

text_file = open("solutions.txt", "w")
text_file.write(output)
text_file.close()