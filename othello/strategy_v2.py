import othello_core as ai
import copy
import random

SQUARE_WEIGHTS = [
    0,          0,   0,   0,  0,  0,  0,  0,   0,               0,

    0,          48,  -15, 6,  6,  6,  6,  -15, 48,              0,
    0,          -15, -24, -4, -4, -4, -4, -24, -15,             0,
    0,          6,   -4,  1,  1,  1,  1,  -4,  6,             0,
    0,          6,   -4,  1,  1,  1,  1,  -4,  6,               0,
    0,          6,   -4,  1,  1,  1,  1,  -4,  6,               0,
    0,          6,   -4,  1,  1,  1,  1,  -4,  6,             0,
    0,          -15, -24, -4, -4, -4, -4, -24, -15,             0,
    0,          48,  -15, 6,  6,  6,  6,  -15, 48,              0,

    0,  0,   0,   0,  0,  0,  0,  0,   0,   0,
]

bval = sum(map(abs, SQUARE_WEIGHTS))
aval = -(bval)


class othelloGame2(ai.OthelloCore):
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
        temp_board = [i for i in board]
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
        # pass

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
        """Compute player's score (number of player's pieces minus opponent's)."""
        otherPlayer = self.opponent(player)
        counter = 0
        for val in board:
            if val is player:
                counter += 1
            if val is otherPlayer:
                counter -= 1
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

    # alpha beta
    def weight(self, p, o, b):
        fnl = 0
        for x in self.squares():
            if b[x] is p:
                fnl += SQUARE_WEIGHTS[x]
            elif b[x] is o:
                fnl -= SQUARE_WEIGHTS[x]
        return fnl

    def terminal_test(self, p, b):
        fnl = self.score(p, b)
        if fnl < 0:
            return aval
        elif fnl > 0:
            return bval
        return fnl

    def alphabeta(self, player, board, alpha, beta, depth):
        if depth is 0:
            return self.weight(player, self.opponent(player), board), None

        def value(board, alpha, beta):
            return -self.alphabeta(self.opponent(player), board, -beta, -alpha, depth - 1)[0]

        m = self.legal_moves(player, board)
        if len(m) is 0:
            if not self.any_legal_move(self.opponent(player), board):
                return self.terminal_test(player, board), None
            return value(board, alpha, beta), None
        fnl = m[0]
        for x in m:
            if alpha >= beta:
                break
            v = value(self.make_move(x, player, list(board)), alpha, beta)
            if v > alpha:
                alpha = v
                fnl = x
        return alpha, fnl

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
                    print('Not a legal move. Input another one.')
        return humanPlayer

    def alphabeta_strategy(self, depth):
        def strategy(board, player):
            return self.alphabeta(player, board, aval, bval, depth)[1]
        return strategy