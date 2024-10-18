# Complete Python Chess Game Code

# chess_pieces.py (embedded for convenience)
class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.color} {type(self).__name__} at ({self.x}, {self.y})"


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)


# chess_game.py (embedded for convenience)
import sys

# Initialize the board (8x8 grid)
BOARD = [[None] * 8 for _ in range(8)]


# Initialize pieces (simplified, only including a few pieces for demonstration)
def init_pieces():
    global BOARD
    BOARD[0][0] = Rook('white', 0, 0)
    BOARD[0][1] = Knight('white', 0, 1)
    BOARD[0][2] = Bishop('white', 0, 2)
    BOARD[0][3] = Queen('white', 0, 3)
    BOARD[0][4] = King('white', 0, 4)
    BOARD[0][5] = Bishop('white', 0, 5)
    BOARD[0][6] = Knight('white', 0, 6)
    BOARD[0][7] = Rook('white', 0, 7)

    BOARD[7][0] = Rook('black', 7, 0)
    BOARD[7][1] = Knight('black', 7, 1)
    BOARD[7][2] = Bishop('black', 7, 2)
    BOARD[7][3] = Queen('black', 7, 3)
    BOARD[7][4] = King('black', 7, 4)
    BOARD[7][5] = Bishop('black', 7, 5)
    BOARD[7][6] = Knight('black', 7, 6)
    BOARD[7][7] = Rook('black', 7, 7)

    for i in range(8):
        BOARD[1][i] = Pawn('white', 1, i)
        BOARD[6][i] = Pawn('black', 6, i)


init_pieces()


# Function to print the current state of the board
def print_board():
    print('  a b c d e f g h')
    for i, row in enumerate(BOARD, start=1):
        print(i, end=' ')
        for cell in row:
            if cell:
                piece_symbol = {
                    King: 'K', Queen: 'Q', Rook: 'R',
                    Bishop: 'B', Knight: 'N', Pawn: 'P'
                }.get(type(cell), ' ')
                print(f"{piece_symbol}{cell.color[0]}", end=' ')
            else:
                print('.', end=' ')
        print()


# Game loop
def game_loop():
    current_player = 'white'
    while True:
        print_board()
        move_from = input(f"Player {current_player}, enter move (e.g., 'e2 e4') or 'quit' to exit: ")
        if move_from.lower() == 'quit':
            sys.exit("Game exited by user.")
        move_from, move_to = move_from.split()
        x1, y1 = ord(move_from[0]) - 97, int(move_from[1]) - 1
        x2, y2 = ord(move_to[0]) - 97, int(move_to[1]) - 1

        # Simplified move validation (no checks for castling, en passant, etc.)
        if BOARD[x1][y1] and BOARD[x1][y1].color == current_player:
            BOARD[x2][y2] = BOARD[x1][y1]
            BOARD[x1][y1] = None



