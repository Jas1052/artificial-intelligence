import othello_core as core
import random

weights = SQUARE_WEIGHTS = [
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

class Strategy99(core.OthelloCore):

    def __init__(self):
        pass

    def is_valid(self, move):
        if move is None:
            return False
        return (move >= 11 and move < 89)

    def opponent(self, player):
        if player == core.BLACK:
            return core.WHITE
        elif player == core.WHITE:
            return core.BLACK

    def find_bracket(self, move, player, board, direction):
        while self.is_valid(move) and self.is_valid(move + direction):
            move += direction
            if board[move] == core.OUTER:
                return None
            if board[move] == player:
                if board[move - direction] == player:
                    return None
                elif board[move - direction] == self.opponent(player):
                    return move

            if board[move] == core.EMPTY:
                return None

        return None

    def is_legal(self, move, player, board):
        if board[move] != core.EMPTY:
            return False
        for i in range(8):
            direction = core.DIRECTIONS[i]
            if self.find_bracket(move, player, board, direction) is not None:
                return True
        return False


    ######################### Making moves ##########################


    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.


    def make_move(self, move, player, board):
        for i in range(8):
            direction = core.DIRECTIONS[i]
            if self.find_bracket(move, player, board, direction):
                board[move] = player
                self.make_flips(move, player, board, direction)

        return board

    def make_flips(self, move, player, board, direction):
        """Flip pieces in the given direction as a result of the move by player."""
        current = move + direction
        while board[current] == self.opponent(player):
            board[current] = player
            current = current + direction

    def legal_moves(self, player, board):
        moves = []
        indices = [i for i, x in enumerate(board) if x == player]

        for square in range(11,89):
            if self.is_legal(square, player, board):
                moves.append(square)

        random.shuffle(moves)
        return moves

    def any_legal_move(self, player, board):
        return len(self.legal_moves(player, board)) != 0

    def next_player(self,board, prev_player):
        next = self.opponent(prev_player)
        if self.any_legal_move(next, board):
            return next
        return prev_player

    def score(self,player, board):
        white = 0
        black = 0
        for i in range(11, 89):
            if board[i] == core.WHITE:
                white += weights[i]
            elif board[i] == core.BLACK:
                black += weights[i]
        return white - black



    ######################### Strategies #############################


    def human(self, player, board):
        moves_list = self.legal_moves(player, board)
        move = input("Where would you like to put a piece? Here are your options: %s " % moves_list)
        return move

    def random(self, player, board):
        moves_list = self.legal_moves(player, board)
        move = random.choice(moves_list)
        return move

    def minimax(self, player, board, maxdepth):
        if player == core.WHITE: move = self.max_dfs(board, player, maxdepth, 0)[1]
        if player == core.BLACK: move = self.min_dfs(board, player, maxdepth, 0)[1]

        return move

    def max_dfs(self, board, player, maxdepth, current_d):
        if current_d == maxdepth or board.count('.') == 0:
            return self.score(player, board), None
        v = -999999999
        move = -1
        for m in self.legal_moves(player, board):
            new_board = [i for i in board]
            self.make_move(m, player, new_board)
            new_value = self.min_dfs(new_board, self.next_player(new_board, player), maxdepth, current_d + 1)[0]

            if new_value > v:
                v = new_value
                move = m
        return v, move

    def min_dfs(self, board, player, maxdepth, current_d):
        if current_d == maxdepth or board.count('.') == 0:
            return self.score(player, board), None
        v = 999999999
        move = -1
        for m in self.legal_moves(player, board):
            new_board = [i for i in board]
            self.make_move(m, player, new_board)
            new_value = self.max_dfs(new_board, self.next_player(new_board, player), maxdepth, current_d + 1)[0]

            if new_value < v:
                v = new_value
                move = m
        return v, move

    def minimax_strategy(self, max_depth):
        def strategy(board, player):
            return self.minimax(player, board, max_depth)

        return strategy









    def abparallel(self, player, board):
        depth = 5
        a = -9999999999
        b = 9999999999
        if player == core.WHITE:
            maxplayer = True
        elif player == core.BLACK:
            maxplayer = False

        v, move = self.pruning(board, depth, a, b, maxplayer, player)
        return move


    def pruning(self, board, depth, alpha, beta, maxplayer, player):
        if depth == 0 or board.count('.') == 0:
            return self.score(player, board), None
        if maxplayer:
            v = -9999999999
            max_child = 0
            for child in self.legal_moves(player, board):
                new_board = [i for i in board]
                new_board[child] = player
                other_v, other_child = self.pruning(new_board, depth-1, alpha, beta, False, self.opponent(player))
                v = max(v, other_v)
                if child is None:
                    max_child = other_child
                elif other_child is None:
                    max_child = child
                else:
                    max_child = max(child, other_child)
                alpha = max(alpha, v)
                if beta > alpha or beta == alpha:
                    break
            return v, max_child

        else:
            v = 9999999999
            min_child = 0
            for child in self.legal_moves(player, board):
                new_board = [i for i in board]
                new_board[child] = player
                other_v, other_child = self.pruning(new_board, depth - 1, alpha, beta, True, self.opponent(player))
                v = min(v, other_v)
                if child is None:
                    min_child = other_child
                elif other_child is None:
                    min_child = child
                else:
                    min_child = min(child, other_child)
                beta = min(beta, v)
                if beta < alpha or beta == alpha:
                    break
            return v, min_child
