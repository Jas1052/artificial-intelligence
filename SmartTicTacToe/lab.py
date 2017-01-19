def terminal_test(board):
    if x_terminal(board): return "X"
    if o_terminal(board): return "O"
    elif not "." in board: return "TIE"