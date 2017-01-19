from core import *

player = "X"
current_depth = 0

def minimax_strategy(max_depth):
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy

def minimax(board, player, maxdepth):
    move = None
    if player == "X":
        move = max_dfs(board, player, maxdepth, current_depth)[1]
    if player == "O":
        move = min_dfs(board, player, maxdepth, current_depth)[1]
    return move

DICTIONARY = {}
def max_dfs(board, player, maxdepth, current_depth):
    if terminal_test(board):
        return winTest(board), None
    v = -10**10
    move = -1
    for m in actions(board):
        new_board = assign(board, m, player)
        if (new_board, player) in DICTIONARY:
            new_value = DICTIONARY[(new_board, player)]
        else:
            new_value = min_dfs(assign(board, m, player), next_player(board, player), maxdepth, current_depth + 1)[0]
            DICTIONARY[(new_board, player)] = new_value
        if new_value > v:
            v = new_value
            move = m
    return v, move

def min_dfs(board, player, maxdepth, current_depth):
    if terminal_test(board):
        return winTest(board), None
    v = 10**10
    move = -1
    for m in actions(board):
        new_board = assign(board, m, player)
        if (new_board, player) in DICTIONARY:
            new_value = DICTIONARY[(new_board, player)]
        else:
            new_value = max_dfs(assign(board, m, player), next_player(board, player), maxdepth, current_depth + 1)[0]
            DICTIONARY[(new_board, player)] = new_value
        if new_value < v:
            v = new_value
            move = m
    return v, move


def actions(board):
    open = []
    b = list(board)
    for i in range(9):
        if b[i] == ".":
            open.append(i)
    return open


def assign(board, m, player):
    if m in actions(board):
        l = list(board)
        l[m] = player
        board = "".join(l)
    return board

def human(board, player):
    index = input("You are " + player + ". What index do you want for your next move (0-8)?")
    return int(index)

def winTest(board):
    if winner(board) is MAX:
        return 1
    if winner(board) is MIN:
        return -1
    elif "." not in board:
        return 0

