from Area import Area
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
import shelve

class Board:
    def __init__(self):
        self.board = []
        bg_color = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

        posy = 0
        for addy in range(8):
            posx = 0
            helper = []
            for addx in range(8):
                helper.append(Area(posx, posy, bg_color[addx]))
                posx += 75
            self.board.append(helper)
            posy += 75
            bg_color = bg_color[::-1]
        self.add_figures()

    def show(self):
        print('[')
        for row in self.board:
            print('[', end='')
            for area in row:
                print(type(area.checker), end=', ')
            print(']', end='')
            print()
        print(']')

    def add_pawns(self):
        row = 1
        for color in range(-1, 2, 2):
            for area in range(8):
                self.board[row][area].checker = Pawn(color, (row, area))
            row = 6

    def add_good_figures(self):
        positions = [0, 1, 2, 7, 6, 5]
        add = 0
        for _ in range(2):
            row = 0
            for color in range(-1, 2, 2):
                self.board[row][positions[add]].checker = Rook(color, (row, positions[add]))
                self.board[row][positions[add + 1]].checker = Knight(color, (row, positions[add + 1]))
                self.board[row][positions[add + 2]].checker = Bishop(color, (row, positions[add + 2]))
                row = 7
            add = 3

    def add_figures(self):
        self.add_pawns()
        self.add_good_figures()
        row = 0
        for color in range(-1,2,2):
            self.board[row][4].checker = King(color, (row, 4))
            self.board[row][3].checker = Queen(color, (row, 3))
            row = 7

    def possible_moves(self, pos, color):
        checker = self.board[pos[0]][pos[1]].checker
        if checker is not None and checker.color == color:
            if abs(checker.val) == 900:
                return checker.normal_move(self.board)
            elif abs(checker.val) == 10:
                return checker.normal_move(self.board) + checker.set_double_move(self.board) + checker.attack_move(self.board)
            else:
                return checker.move(self.board)
        else:
            return []

