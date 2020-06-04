def is_area_in_board(area):
    if 0 <= area[0] <= 7 and 0 <= area[1] <= 7:
        return True
    return False


def cancel_castling(checker):
    if abs(checker.val) == 50 or abs(checker.val) == 900:
        checker.castling = False

def is_king_beaten(board, color):
    for row in board:
        for area in row:
            if area.checker is not None and area.checker.color != color:  # wedlug Pycharm is not
                if area.checker.king_attack(board):
                    return True
    return False


class Engine:
    def __init__(self):
        self.b_check = False
        self.b_move_check = 0
        self.w_check = False
        self.w_move_check = 0
        self.move_count = 0
        self.win = 1

    def what_kind_of_move(self, prev_pos, new_pos, board):
        checker = board[prev_pos[0]][prev_pos[1]].checker
        if abs(checker.val) == 10 and new_pos in checker.set_passe(board, self.move_count):
            return 'Passe'
        elif abs(checker.val) == 900 and new_pos in checker.set_castling(board):
            return 'Castling'
        else:
            return 'Normal'

    def normal_move(self, prev_pos, new_pos, board):
        checker = board[prev_pos[0]][prev_pos[1]].checker
        cancel_castling(checker)
        checker.pos = new_pos
        board[prev_pos[0]][prev_pos[1]].checker = None
        board[new_pos[0]][new_pos[1]].checker = checker

    def move_checker(self, prev_pos, new_pos, board):
        checker = board[prev_pos[0]][prev_pos[1]].checker
        if abs(checker.val) == 10:
            self.passe_move(prev_pos, new_pos, board)
        elif abs(checker.val) == 900:
            self.castling_move(prev_pos, new_pos, board)
        else:
            self.normal_move(prev_pos, new_pos, board)
        self.move_count += 1

    def castling_move(self, prev_pos, new_pos, board):
        if new_pos in board[prev_pos[0]][prev_pos[1]].checker.set_castling(board):
            row = 0
            if self.which_tour() == 1:
                row = 7
            board[row][4].checker.castling = False
            self.normal_move((row, 4), new_pos, board)
            if new_pos[1] == 2:
                self.normal_move((row, 0), (row, 3), board)
            else:
                self.normal_move((row, 7), (row, 5), board)
        else:
            self.normal_move(prev_pos, new_pos, board)

    def passe_move(self, prev_pos, new_pos, board):
        if new_pos in board[prev_pos[0]][prev_pos[1]].checker.set_double_move(board):
            board[prev_pos[0]][prev_pos[1]].checker.move_passe = self.move_count
            self.normal_move(prev_pos, new_pos, board)

        elif new_pos in board[prev_pos[0]][prev_pos[1]].checker.set_passe(board, self.move_count):
            self.normal_move(prev_pos, new_pos, board)
            color = board[new_pos[0]][new_pos[1]].checker.color
            board[new_pos[0] + 1 * color][new_pos[1]].checker = None

        else:
            self.normal_move(prev_pos, new_pos, board)
            board[new_pos[0]][new_pos[1]].checker.is_promotion(board)

    def is_check(self, w_king_beat, b_king_beat):
        if w_king_beat and b_king_beat:
            if self.w_check is False and self.b_check is False:
                self.w_check = True
                self.w_move_check = self.move_count
                self.b_check = True
                self.b_move_check = self.move_count
        elif w_king_beat and self.w_check is False:
            self.w_check = True
            self.w_move_check = self.move_count
            self.b_check = False
            self.b_move_check = 0
        elif b_king_beat and self.b_check is False:
            self.b_check = True
            self.b_move_check = self.move_count
            self.w_check = False
            self.w_move_check = 0

    def is_checkmate(self):
        if self.w_check is True and self.move_count != self.w_move_check and self.move_count - self.w_move_check <= 2:
            self.win = -1
            return True
        elif self.b_check is True and self.move_count != self.b_move_check and self.move_count - self.b_move_check <= 2:
            self.win = 1
            return True
        else:
            return False

    def is_end(self, board):
        w_king_beat = is_king_beaten(board, 1)
        b_king_beat = is_king_beaten(board, -1)
        if w_king_beat or b_king_beat:
            self.is_check(w_king_beat, b_king_beat)
            return self.is_checkmate()
        self.w_check = False
        self.w_move_check = 0
        self.b_check = False
        self.b_move_check = 0
        return False

    def which_tour(self):
        if self.move_count % 2 == 0:
            return 1
        else:
            return -1

    def copy(self):
        copy = Engine()
        copy.b_check = self.b_check
        copy.b_move_check = self.b_move_check
        copy.w_check = self.w_check
        copy.w_move_check = self.w_move_check
        copy.move_count = self.move_count
        copy.win = self.win
        return copy

    def value_of_table(self, board, bot):
        ans = 0
        for row in range(8):
            for area in range(8):
                if board[row][area].checker is not None:
                    ans += board[row][area].checker.val #+ bot.get_position_val(board[row][area].checker)
        return ans

    def back_move(self, prev_pos, now_pos, move_checker, beat_checker, board):
        board[prev_pos[0]][prev_pos[1]].checker = move_checker
        board[now_pos[0]][now_pos[1]].checker = beat_checker
        self.move_count -= 1

