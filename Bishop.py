from Engine import is_area_in_board


class Bishop:
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.val = 30 * self.color
        self.image_id = self.create_image_id()

    def create_image_id(self):
        return 17 + self.color

    def move(self, board):
        moves = []
        directions = [1, 1, -1, -1, 1, -1, -1, 1]
        for i in range(0, len(directions), 2):
            for j in range(1, 8):
                area = (self.pos[0] + j * directions[i], self.pos[1] + j * directions[i + 1])
                if is_area_in_board(area):
                    if board[area[0]][area[1]].checker == None:  # wedlug Pcharm is
                        moves.append(area)
                    else:
                        if board[area[0]][area[1]].checker.color != self.color:
                            if board[area[0]][area[1]].checker.val != 900 * self.color * -1:
                                moves.append(area)
                        break
                else:
                    break

        return moves

    def king_attack(self, board):
        directions = [1, 1, -1, -1, 1, -1, -1, 1]
        for i in range(0, len(directions), 2):
            for j in range(1, 8):
                area = (self.pos[0] + j * directions[i], self.pos[1] + j * directions[i + 1])
                if is_area_in_board(area):
                    if board[area[0]][area[1]].checker == None:  # wedlug Pcharm is
                        continue
                    else:
                        if board[area[0]][area[1]].checker.color != self.color:
                            if board[area[0]][area[1]].checker.val == 900 * self.color * -1:
                                return True
                        break
                else:
                    break

        return False

    def copy(self):
        return Bishop(self.color, self.pos)
