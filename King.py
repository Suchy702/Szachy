from Engine import is_area_in_board
from Engine import is_king_beaten


class King:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.val = 900 * self.color
        self.image_id = self.create_image_id()
        self.castling = True

    def create_image_id(self):
        return 1 + self.color

    def move(self, board):
        return self.normal_move(board) + self.set_castling(board)

    def normal_move(self, board):
        moves = []
        correct_moves = []
        directions = [1, 0, -1, 0, 0, 1, 0, -1, 1, 1, -1, -1, 1, -1, -1, 1]
        for i in range(0, len(directions), 2):
            moves.append((self.pos[0] + directions[i], self.pos[1] + directions[i + 1]))

        for area in moves:
            if is_area_in_board(area):
                if board[area[0]][area[1]].checker is None:
                    correct_moves.append(area)
                elif board[area[0]][area[1]].checker.color != self.color:
                    if board[area[0]][area[1]].checker.val != 900 * self.color * -1:
                        correct_moves.append(area)
        return correct_moves

    def set_castling(self, board):
        castling_moves = []

        if self.castling and not is_king_beaten(board, self.color):
            row = 0
            if self.color == 1:
                row = 7
            if board[row][0].checker is not None:
                if abs(board[row][0].checker.val) == 50 and board[row][0].checker.castling is True:
                    if board[row][1].checker == board[row][2].checker == board[row][3].checker is None:
                        if not self.attack_castling_areas([(row, 1), (row, 2), (row, 3)], board):
                            castling_moves.append((row, 2))
            if board[row][7].checker is not None:
                if abs(board[row][7].checker.val) == 50 and board[row][7].checker.castling is True:
                    if board[row][5].checker == board[row][6].checker is None:
                        if not self.attack_castling_areas([(row, 5), (row, 6)], board):
                            castling_moves.append((row, 6))
        return castling_moves

    def king_attack(self, board):
        moves = []
        directions = [1, 0, -1, 0, 0, 1, 0, -1, 1, 1, -1, -1, 1, -1, -1, 1]
        for i in range(0, len(directions), 2):
            moves.append((self.pos[0] + directions[i], self.pos[1] + directions[i + 1]))

        for area in moves:
            if is_area_in_board(area):
                if board[area[0]][area[1]].checker is not None:
                    if board[area[0]][area[1]].checker.color != self.color:
                        if board[area[0]][area[1]].checker.val == 900 * self.color * -1:
                            return True
        return False

    def attack_castling_areas(self, death_areas, board):
        for row in board:
            for area in row:
                if area.checker is not None and area.checker.color != self.color:
                    if abs(area.checker.val) == 10:
                        enemies_moves = area.checker.attack_move(board)
                    elif abs(area.checker.val) == 900:
                        enemies_moves = area.checker.normal_move(board)
                    else:
                        enemies_moves = area.checker.move(board)
                    for death in death_areas:
                        if death in enemies_moves:
                            return True
        return False

    def copy(self):
        return King(self.color, self.pos)
