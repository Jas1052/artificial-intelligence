
import pickle
import random
from time import time
from jliu_strategy import Strategy      # first file
# from rehan_strategy import Strategy99  # second file
import othello_core as core

tic = time()
ROUNDS = 1
SILENT = False

s = Strategy()   # name of class in first strategy
v = Strategy()  # name of class in second strategy

s1 = s.alphabeta_strategy(5)    # actually calling of method in class; returns a strategy method
s2 = v.human_strategy(3)    # ditto

def play(strategy_X, strategy_O, first, silent=True):
    """
    Plays strategy_X vs. strategy_O, beginning with first
    in one game. Returns X, O or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """

    board = s.initial_board()
    player = first
    current_strategy = {first: strategy_X, s.opponent(first): strategy_O}
    print(s.print_board(board))
    while board.count('.') != 0 and (len(s.legal_moves('o', board)) > 0 or len(v.legal_moves('@', board)) > 0):
        move = current_strategy[player](board, player)
        board = s.make_move(move, player, board)
        print(player + " makes move at " + str(move))
        player = s.opponent(player)
        if not silent: print(s.print_board(board))
    return s.score('o', board)  # returns the score


def main():
    """
    Plays ROUNDS tic-tac-toe games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """
    j = []
    for i in range(ROUNDS):
            game_result = play(s1, s2,
                          first=random.choice([core.WHITE, core.WHITE]),
                          silent=SILENT)
            print(game_result)
            if game_result > 0: game_result = core.WHITE
            elif game_result < 0: game_result = core.BLACK

            j.append(game_result)
            print("Winner: ", game_result, "\n")

    print("\nResults\n" + "%4s %4s %4s" % ("o", "@", "-"))
    print("-" * 15)
    print("%4i %4i %4i" % (j.count(core.WHITE), j.count(core.BLACK), j.count(0)))
    toc = time()
    print("Time:", toc-tic, " seconds")


if __name__ == "__main__":
    main()
