from Engine import is_area_in_board


class Knight:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.val = 30 * self.color
        self.image_id = self.create_image_id()

    def create_image_id(self):
        return 13 + self.color

    def move(self, board):
        moves = []
        correct_moves = []
        directions = [2, 1, 2, -1, -2, 1, -2, -1, 1, 2, 1, -2, -1, 2, -1, -2]
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

    def king_attack(self, board):
        moves = []
        directions = [2, 1, 2, -1, -2, 1, -2, -1, 1, 2, 1, -2, -1, 2, -1, -2]
        for i in range(0, len(directions), 2):
            moves.append((self.pos[0] + directions[i], self.pos[1] + directions[i + 1]))

        for area in moves:
            if is_area_in_board(area):
                if board[area[0]][area[1]].checker is not None and board[area[0]][area[1]].checker.color != self.color:
                    if board[area[0]][area[1]].checker.val == 900 * self.color * -1:
                        return True
        return False

    def copy(self):
        return Knight(self.color, self.pos)
