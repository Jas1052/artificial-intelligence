import othello_core as ai
import copy
import random

SQUARE_WEIGHTS = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

class Strategy(ai.OthelloCore):
    def __init__(self, board=None):
        if board is None:
            board = self.initial_board()
        else:
            board = board
        self.DICTIONARY = {}
        self.current_depth = 0

    def createBoard(self):
        self.DICTIONARY = {}
        board = self.initial_board()
        self.current_depth = 0
        self.print_board(board)


    def is_valid(self, move):
        """Is move a square on the board?"""
        return move >= 11 and move <= 89

    def opponent(self, player):
        """Get player's opponent piece."""
        if player is '@':
            return 'o'
        if player is 'o':
            return '@'

    def find_bracket(self, square, player, board, direction):
        """
        Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found
        """
        # UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
        # UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
        opponent = self.opponent(player)
        middle = square
        if board[middle + direction] is not opponent:
            return None
        else:
            while board[middle + direction] is opponent:
                middle += direction
            if board[middle+direction] is player:
                return middle
            else:
                return None

    def is_legal(self, move, player, board):
        """Is this a legal move for the player?"""
        # UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
        # UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
        if self.is_valid(move) is False or board[move] is not '.':
            return False
        if self.find_bracket(move, player, board, -10) is not None:
            return True
        if self.find_bracket(move, player, board, 10) is not None:
            return True
        if self.find_bracket(move, player, board, -1) is not None:
            return True
        if self.find_bracket(move, player, board, 1) is not None:
            return True
        if self.find_bracket(move, player, board, -9) is not None:
            return True
        if self.find_bracket(move, player, board, 11) is not None:
            return True
        if self.find_bracket(move, player, board, 9) is not None:
            return True
        if self.find_bracket(move, player, board, -11) is not None:
            return True
        return False

    ### Making moves

    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.

    def make_move(self, move, player, board):
        """Update the board to reflect the move by the specified player."""
        temp_board = board
        if move is not None:
            self.make_flips(move, player, temp_board, 10)
            self.make_flips(move, player, temp_board, -10)
            self.make_flips(move, player, temp_board, 1)
            self.make_flips(move, player, temp_board, -1)
            self.make_flips(move, player, temp_board, 11)
            self.make_flips(move, player, temp_board, -11)
            self.make_flips(move, player, temp_board, 9)
            self.make_flips(move, player, temp_board, -9)
            temp_board[move] = player
            # print(player + self.print_board(temp_board))
            return temp_board
        else:
            return temp_board

    def make_flips(self, move, player, board, direction):
        """Flip pieces in the given direction as a result of the move by player."""
        if self.find_bracket(move, player, board, direction) is not None:
            opponent = self.opponent(player)
            middle = move + direction
            while board[middle] is opponent:
                board[middle] = player
                middle += direction

    def legal_moves(self, player, board):
        """Get a list of all legal moves for player, as a list of integers"""
        output = []
        for i in range(11, 89):
            if self.is_legal(i, player, board):
                output.append(i)
        return random.sample(output, len(output))

    def any_legal_move(self, player, board):
        """Can player make any moves? Returns a boolean"""
        if len(self.legal_moves(player, board)) is 0:
            return False
        else:
            return True

    def next_player(self, board, prev_player):
        """Which player should move next?  Returns None if no legal moves exist."""
        player = ''
        if prev_player is '@':
            player = 'o'
        if prev_player is 'o':
            player = '@'
        if self.any_legal_move(player, board):
            return player
        else:
            return None

    def determine_winner(self, board):
        player1 = 0
        player2 = 0
        for val in board:
            if val is 'o':
                player1 += 1
            if val is '@':
                player2 += 2
        if player1 > player2:
            return 'o'
        else:
            return '@'

    def score(self, player, board):
        """Compute player's score (current_depthber of player's pieces minus opponent's)."""
        otherPlayer = self.opponent(player)
        counter = 0
        for val in board:
            if val is player:
                counter += 1
            if val is otherPlayer:
                counter -= 1
        return counter

    def weigh(self, board):
        counter = 0
        for i in range(11, 88):
            if board[i] is '@':
                counter -= SQUARE_WEIGHTS[i]
            if board[i] is 'o':
                counter += SQUARE_WEIGHTS[i]
        return counter

    def randomMove(self, player, board):
        legalMoves = self.legal_moves(player, board)
        rand = random.randint(0, len(legalMoves)-1)
        move = legalMoves[rand]
        self.make_move(move, player, board)
        self.make_flips(move, player, board, 10)
        self.make_flips(move, player, board, -10)
        self.make_flips(move, player, board, 1)
        self.make_flips(move, player, board, -1)
        self.make_flips(move, player, board, 11)
        self.make_flips(move, player, board, -11)
        self.make_flips(move, player, board, 9)
        self.make_flips(move, player, board, -9)

    def human_strategy(self, depth):
        def humanPlayer(board, player):
            print('Your Move: ' + player)
            while(True):
                y = int(input("y-coord: "))
                x = int(input("x-coord: "))
                move = 10*y + x
                if move in self.legal_moves(player, board):
                    return 10*y + x
                else:
                    print('Not a legal move. Try again.')
        return humanPlayer

    def best_strategy(self, board, player, best_move, still_running):
        """
            :param board: a length 100 list representing the board state
            :param player: WHITE or BLACK
            :param best_move: shared multiptocessing.Value containing an int of
                    the current best move
            :param still_running: shared multiprocessing.Value containing an int
                    that is 0 iff the parent process intends to kill this process
            :return: best move as an int in [11,88] or possibly 0 for 'unknown'
        """
        """while still_running is not 0:
            depth = 5
            best_move.value = self.alpha_beta(board, player, depth)
            depth += 1
        """
        depth = 3
        while still_running is not 0:
            val = self.alpha_beta(board, player, depth)
            best_move.value = val
            depth += 1
        return

    def alpha_beta(self, board, player, depth):
        if player is 'o':
            v, m = self.max_value(board, player, -10**10, 10**10, depth, 0)
            if m is None:
                return 0
            return m
        if player is '@':
            v, m = self.min_value(board, player, -10**10, 10**10, depth, 0)
            if m is None:
                return 0
            return m

    def max_value(self, board, player, alpha, beta, depth, current_depth):
        if self.next_player(board, player) is None or current_depth is depth:
            return self.weigh(board), None
        v = -10**10
        move = None
        for val in self.legal_moves(player, board):
            tempv = v
            tempBoard = [board[i] for i in range(len(board))]
            tempBoard = self.make_move(val, player, tempBoard)
            v = max(v, self.min_value(tempBoard, self.next_player(tempBoard, player), alpha, beta, depth, current_depth + 1)[0])
            if tempv is not v:
                move = val
            if v >= beta:
                return v, val
            alpha = max(alpha, v)
        return v, move

    def min_value(self, board, player, alpha, beta, depth, current_depth):
        if self.next_player(board, player) is None or current_depth is depth:
            return self.weigh(board), None
        v = 10**10
        move = None
        for val in self.legal_moves(player, board):
            tempv = v
            tempBoard = [board[i] for i in range(len(board))]
            tempBoard = self.make_move(val, player, tempBoard)
            v = min(v, self.max_value(tempBoard, self.next_player(tempBoard, player), alpha, beta, depth, current_depth + 1)[0])
            if tempv is not v:
                move = val
            if alpha >= v:
                return v, val
            beta = min(beta, v)
        return v, move

    def alphabeta_strategy(self, depth):
        def strategy(board, player):
            return self.alpha_beta(board, player, depth)
        return strategy
