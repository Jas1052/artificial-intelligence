from server import *
import sys


board = ttt()
print(board)

while board.isNotEmpty():
    #user move
    y = input("y-coord: ")
    x = input("x-coord: ")
    board.userInput(int(y), int(x))
    print(board)
    print('\n')
    if(board.userWin()):
        print('You Win!')
        break
              
    # computer move
    coords = board.getNextMove()
    y = coords[0]
    x = coords[1]
    board.cpuInput(y, x)
    print('Computer has Moved:')
    print(board)
    print('\n')
    if(board.cpuWin()):
        print('You Lose')
        break
