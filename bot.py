class Bot:
    def __init__(self):
        self.positions_val = [
            [
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
                [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
                [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
                [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
                [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
                [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            ],

            [
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
                [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
                [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
                [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
                [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
                [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
            ],

            [
                [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
                [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
                [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
                [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
                [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
                [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
            ],

            [
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
                [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
            ],

            [
                [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
                [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
                [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
                [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
                [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
                [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
            ],

            [
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
                [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
                [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
                [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
            ]]

    def move(self, engine, gui, board):
        if engine.move_count < 4:
            min_start, min_end = self.opening_moves(engine.move_count)
        else:
            c_engine = engine.copy()
            (m, min_start, min_end) = self.find_best_move(3, board, c_engine, -9999, 9999, False)
        move_type = engine.what_kind_of_move(min_start, min_end, board.board)
        start = board.board[min_start[0]][min_start[1]]
        end = board.board[min_end[0]][min_end[1]]
        gui.kind_of_animation(start, end, move_type, board.board)
        engine.move_checker(min_start, min_end, board.board)

    def find_best_move(self, depth, board, engine, alpha, beta, maximize):
        if maximize:
            maxv = -9999

            start_pos = None
            end_pos = None

            end = engine.is_end(board.board)
            if depth == 0 or end:
                if end:
                    return engine.value_of_table(board.board, self) + engine.win * 900, (0, 0), (0, 0)
                return engine.value_of_table(board.board, self), (0, 0), (0, 0)

            for row in range(8):
                for column in range(8):
                    moves = board.possible_moves((row, column), 1)
                    if len(moves) != 0:
                        for move in moves:
                            moving_checker = board.board[row][column].checker.copy()
                            beat_checker = None
                            if board.board[move[0]][move[1]].checker is not None:
                                beat_checker = board.board[move[0]][move[1]].checker.copy()
                            engine.normal_move((row, column), move, board.board)
                            (val, start, end) = self.find_best_move(depth - 1, board, engine.copy(), alpha, beta, False)
                            if val > maxv:
                                maxv = val
                                start_pos = (row, column)
                                end_pos = move

                            engine.back_move((row, column), move, moving_checker, beat_checker, board.board)

                        if maxv >= beta:
                            return maxv, start_pos, end_pos

                        if maxv > alpha:
                            alpha = maxv

            return maxv, start_pos, end_pos
        else:
            minv = 9999

            start_pos = None
            end_pos = None

            end = engine.is_end(board.board)
            if depth == 0 or end:
                if end:
                    return engine.value_of_table(board.board, self) + engine.win * 900, (0, 0), (0, 0)
                return engine.value_of_table(board.board, self), (0, 0), (0, 0)

            for row in range(8):
                for column in range(8):
                    moves = board.possible_moves((row, column), -1)
                    if len(moves) != 0:
                        for move in moves:
                            moving_checker = board.board[row][column].checker.copy()
                            beat_checker = None
                            if board.board[move[0]][move[1]].checker is not None:
                                beat_checker = board.board[move[0]][move[1]].checker.copy()
                            engine.normal_move((row, column), move, board.board)
                            (val, start, end) = self.find_best_move(depth - 1, board, engine.copy(), alpha, beta, True)
                            if val < minv:
                                minv = val
                                start_pos = (row, column)
                                end_pos = move
                            engine.back_move((row, column), move, moving_checker, beat_checker, board.board)

                            if minv <= alpha:
                                return minv, start_pos, end_pos

                            if minv < beta:
                                beta = minv

            return minv, start_pos, end_pos

    def opening_moves(self, move_count):
        if move_count == 1:
            return (1, 3), (3, 3)
        else:
            return (1, 2), (2, 2)

    def reverse(self, table):
        ans = []
        for row in range(len(table) - 1, -1, -1):
            ans.append(table[row][::-1])
        return ans

    def get_position_val(self, checker):
        id = checker.create_image_id()
        row = checker.pos[0]
        column = checker.pos[1]
        types = [(22, 20), (14, 12), (18, 16), (10, 8), (6, 4), (0, 2)]
        for i in range(len(types)):
            if id == types[i][0]:
                return self.positions_val[i][row][column]
            elif id == types[i][1]:
                return self.reverse(self.positions_val[i])[row][column]
