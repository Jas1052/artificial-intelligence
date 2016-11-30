import time

gamesCounter = 0
boards = set([])

def findTTT(board, move):
    if end(board, 'O'):
        global gamesCounter
        gamesCounter += 1
        boards.add(str(board))
    else:
        if end(board, 'X'):
            global gamesCounter
            gamesCounter += 1
            boards.add(str(board))
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = move
                        nextMove = ''
                        if move == 'O':
                            nextMove = 'X'
                        if move == 'X':
                            nextMove = 'O'
                        findTTT(board, nextMove)
                        board[i][j] = ''

def end(board, player):
    for i in range(3):
        tempBool = True
        for j in range(3):
            if board[i][j] != player:
                tempBool = False
        if tempBool is True:
            return True
    for j in range(3):
        tempBool = True
        for i in range(3):
            if board[i][j] != player:
                tempBool = False
        if tempBool is True:
            return True

    tempBool = True
    for i in range(3):
        if board[i][i] != player:
            tempBool = False
    if tempBool is not False:
        return True

    tempBool = True
    for i in range(3):
        if board[i][2 - i] != player:
            tempBool = False
    if tempBool is not False:
        return True

    tempBool = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                tempBool = False
    if tempBool is not False:
        return True

start = time.time()
findTTT([['', '', ''],
         ['', '', ''],
         ['', '', '']], 'X')
stop = time.time()

print("Time: " + str(stop - start))
print("Games: " + str(gamesCounter))
print("Boards: " + str(len(boards)))

# 255168 Games

