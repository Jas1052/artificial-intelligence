class ttt:
    def __init__(self):
            self.board = [[-1,-1,-1],
                          [-1,-1,-1],
                          [-1,-1,-1]]

    def __str__(self):
        output = ''
        for y in range(3):
            output = output + '\n'
            for x in range(3):
                if self.board[y][x] == -1:
                    output = output + '[  ]'
                if self.board[y][x] == 0:
                    output = output + '[O]'
                if self.board[y][x] == 1:
                    output = output + '[X]'
        return output

    def getNextMove(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == -1:
                    return (y, x)

    def checkValid(self, y, x):
        if self.board[y][x] == -1:
            return True
        else:
            return False

    def userInput(self, y, x):
        self.board[y][x] = 1

    def cpuInput(self, y, x):
        self.board[y][x] = 0

    def isNotEmpty(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == -1:
                    return True
        return False
    
    def userWin(self):
        for y in range(3):
            if self.board[y][0] == self.board[y][1] and self.board[y][1] == self.board[y][2] and self.board[y][2] == 1:
                return True
        for x in range(3):
            if self.board[0][x] == self.board[1][x] and self.board[1][x] == self.board[2][x] and self.board[2][x] == 1:
                return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] == 1:
            return True
        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[0][2] == 1:
            return True
        return False
    
    def cpuWin(self):
        for y in range(3):
            if self.board[y][0] == self.board[y][1] and self.board[y][1] == self.board[y][2] and self.board[y][2] == 0:
                return True
        for x in range(3):
            if self.board[0][x] == self.board[1][x] and self.board[1][x] == self.board[2][x] and self.board[2][x] == 0:
                return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] == 0:
            return True
        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[0][2] == 0:
            return True
        return False
