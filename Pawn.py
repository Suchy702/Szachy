from Engine import is_area_in_board
from Queen import Queen


class Pawn:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.val = 10 * self.color
        self.image_id = self.create_image_id()
        self.move_passe = -1

    def create_image_id(self):
        return 21 + self.color

    def move(self, board, move_count):
        normal_moves = self.normal_move(board) + self.attack_move(board)
        return normal_moves + self.set_double_move(board) + self.set_passe(board, move_count)

    def normal_move(self, board):
        correct_moves = []
        direction = self.color * - 1

        area = (self.pos[0] + 1 * direction, self.pos[1])
        if is_area_in_board(area) and board[area[0]][area[1]].checker is None:
            correct_moves.append(area)

        return correct_moves

    def attack_move(self, board):
        correct_attacks = []
        direction = self.color * - 1
        moves = [(self.pos[0] + 1 * direction, self.pos[1] + 1),
                 (self.pos[0] + 1 * direction, self.pos[1] - 1)]
        for area in moves:
            if is_area_in_board(area) and board[area[0]][area[1]].checker is not None:
                if board[area[0]][area[1]].checker.color != self.color:
                    if board[area[0]][area[1]].checker.val != 900 * self.color * -1:
                        correct_attacks.append(area)
        return correct_attacks

    def set_passe(self, board, move_count):
        passe_moves = []
        passe_attack = 3
        if self.color == -1:
            passe_attack = 4

        moves = [(self.pos[0], self.pos[1] + 1),
                 (self.pos[0], self.pos[1] - 1)]

        for area in moves:
            if is_area_in_board(area) and self.pos[0] == passe_attack and board[area[0]][area[1]].checker is not None:
                if abs(board[area[0]][area[1]].checker.val) == 10 and board[area[0]][area[1]].checker.move_passe != -1:
                    if move_count - board[area[0]][area[1]].checker.move_passe <= 2:
                        passe_moves.append((area[0] - 1 * self.color, area[1]))

        return passe_moves

    def set_double_move(self, board):
        double_move = []
        start = 6
        if self.color == -1:
            start = 1

        if self.pos[0] == start:
            if board[(self.pos[0] + 1 * self.color * -1)][self.pos[1]].checker is None:  # Wedlug Pycharm is
                if board[(self.pos[0] + 2 * self.color * -1)][self.pos[1]].checker is None:  # Wedlug Pycharm is
                    double_move.append((self.pos[0] + 2 * self.color * -1, self.pos[1]))

        return double_move

    def king_attack(self, board):
        self.is_promotion(board)
        direction = self.color * - 1

        moves = [(self.pos[0] + 1 * direction, self.pos[1] + 1),
                 (self.pos[0] + 1 * direction, self.pos[1] - 1)]

        for area in moves:
            if is_area_in_board(area) and board[area[0]][area[1]].checker is not None:  # Wedlug Pycharm is not
                if board[area[0]][area[1]].checker.color != self.color:
                    if board[area[0]][area[1]].checker.val == 900 * self.color * -1:
                        return True

        return False

    def is_promotion(self, board):
        if self.color == 1 and self.pos[0] == 0:
            board[self.pos[0]][self.pos[1]].checker = Queen(1, self.pos)
        elif self.color == -1 and self.pos[0] == 7:
            board[self.pos[0]][self.pos[1]].checker = Queen(-1, self.pos)

    def copy(self):
        return Pawn(self.color, self.pos)
