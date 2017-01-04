import pickle
import strategy7_jjliu as ai
from core import *

#############################################################
# client.py
# a simple tic-tac-toe client
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
# rest of functionality is stored in core.py
#
# Patrick White: December 2016
############################################################

X_STRATEGY = ai.minimax_strategy(3)
O_STRATEGY = ai.minimax_strategy(3)
ROUNDS = 10
SILENT = False

# see core.py for constants: MAX, MIN, TIE

def play(strategy_X, strategy_O, first=MAX, silent=True):
    """
    Plays strategy_X vs. strategy_O, beginning with first
    in one game. Returns X, O or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """
    board = start_state
    player = first
    current_strategy = {MAX: strategy_X, MIN: strategy_O}
    while player is not None:
        move = current_strategy[player](board, player)
        board = make_move(board, player, move)
        player = next_player(board, player)
        if not silent: print_board(board)
    return terminal_test(board) # returns "X" "O" or "TIE"


def main():
    """
    Plays ROUNDS tic-tac-toe games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """
    j = []
    for i in range(ROUNDS):
        try:
            game_result = play(X_STRATEGY, O_STRATEGY,
                          first=random.choice([MAX, MIN]),
                          silent=SILENT)
            j.append(game_result)
            print("Winner: ", game_result)
        except IllegalMoveError as e:
            print(e)
            j.append("FORFEIT")
    print("\nResults\n" + "%4s %4s %4s" % ("X", "O", "-"))
    print("-" * 15)
    print("%4i %4i %4i" % (j.count(MAX), j.count(MIN), j.count(TIE)))


if __name__ == "__main__":
    main()