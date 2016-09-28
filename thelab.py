import heapq

class value:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        if len(self.word) < len(other.getWord()):
            return True
        else:
            return False

    def getWord(self):
        return self.word


heap = []

heapq.heappush(heap, value("word"))
heapq.heappush(heap, value("longerword"))
heapq.heappush(heap, value("hi"))
heapq.heappush(heap, value("wor"))
heapq.heappush(heap, value("elijdlke"))

# pop them off, in order
while heap:
    print(heapq.heappop(heap).getWord())