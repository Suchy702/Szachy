import pygame


class Events:
    def __init__(self):
        self.prev_clik = None
        self.possible_moves = []

        self.play_again = None

        self.choose_who_you_want_to_play_with = False
        self.play_wiht_bot = False
        self.someone_win = False
        self.done = False

        self.figure_dragging = False
        self.mid_x = 0
        self.mid_y = 0
        self.start_drag = None
        self.drag_im_id = None
        self.dif = 0
        self.prev_place = (10000, 10000)
        self.dragged = False

    def where_clik(self, pos):
        y_up, y_down = 0, 75
        for y in range(8):
            x_left, x_right = 0, 75
            for x in range(8):
                if y_up <= pos[0] <= y_down and x_left <= pos[1] <= x_right:
                    return x, y
                x_left += 75
                x_right += 75
            y_up += 75
            y_down += 75
        return 'Nowhere'

    def choose_want_play_again(self, pos):
        if 8 <= pos[0] <= 225 and 273 <= pos[1] <= 359:
            return True
        elif 415 <= pos[0] <= 625 and 273 <= pos[1] <= 359:
            return False
        else:
            return None

    def move_reaction(self, pos, gui, engine, board, animation):
        move_type = engine.what_kind_of_move(self.prev_clik, pos, board)
        self.clear_pos_moves(self.possible_moves, board)
        if animation:
            gui.kind_of_animation(board[self.prev_clik[0]][self.prev_clik[1]], board[pos[0]][pos[1]], move_type, board)
        engine.move_checker(self.prev_clik, pos, board)
        gui.show_board(board)
        self.possible_moves = []
        pygame.display.update()

    def set_poss_moves(self, pos, engine, board):
        if abs(board[pos[0]][pos[1]].checker.val) == 10:
            self.possible_moves = board[pos[0]][pos[1]].checker.move(board, engine.move_count)
        elif abs(board[pos[0]][pos[1]].checker.val) == 900:
            self.possible_moves = board[pos[0]][pos[1]].checker.move(board)
        else:
            self.possible_moves = board[pos[0]][pos[1]].checker.move(board)

    def set_new_target(self, pos, gui, engine, board):
        self.set_poss_moves(pos, engine, board)
        gui.show_board(board)
        gui.show_possible_moves(self.possible_moves, board)
        pygame.display.update()
        self.prev_clik = pos

    def set_prev_clik(self, pos, gui, board):
        self.prev_clik = pos
        self.clear_pos_moves(self.possible_moves, board)
        self.possible_moves = []
        gui.show_board(board)
        pygame.display.update()

    def what_to_do(self, pos, gui, engine, board, animation):
        color = engine.which_tour()
        if pos == 'Nowhere':
            return
        if pos in self.possible_moves:
            self.move_reaction(pos, gui, engine, board, animation)
        elif board[pos[0]][pos[1]].checker is not None and board[pos[0]][pos[1]].checker.color == color:
            self.set_new_target(pos, gui, engine, board)
        else:
            self.set_prev_clik(pos, gui, board)

    def clear_pos_moves(self, pos_moves, board):
        for pos in pos_moves:
            board[pos[0]][pos[1]].showing_possible_move = False

    def pre_drag(self, pos_click, gui, engine, board):
        color = engine.which_tour()
        pos = self.where_clik(pos_click)
        self.what_to_do(pos, gui, engine, board, True)
        if board[pos[0]][pos[1]].checker is not None and board[pos[0]][pos[1]].checker.color == color:
            if len(self.possible_moves) != 0:
                self.mid_x = abs(pos_click[0] - board[pos[0]][pos[1]].posx)
                self.mid_y = abs(pos_click[1] - board[pos[0]][pos[1]].posy)
                self.start_drag = board[pos[0]][pos[1]]
                self.figure_dragging = True
                self.drag_im_id = board[pos[0]][pos[1]].checker.image_id

    def dragging(self, pos_drag, gui, board):
        if self.figure_dragging:
            self.dif = abs(pos_drag[0] - self.prev_place[0]) + abs(pos_drag[1] - self.prev_place[1])
            if self.dif > 25:
                gui.show_board(board)
            else:
                gui.update(gui.what_must_update((pos_drag[0] - self.mid_x, pos_drag[1] - self.mid_y), board, 'big'), board)
            gui.screen.blit(gui.bg_images[self.start_drag.bg_color()], (self.start_drag.posx, self.start_drag.posy))
            gui.show_possible_moves(self.possible_moves, board)
            gui.show_figure((pos_drag[0] - self.mid_x, pos_drag[1] - self.mid_y), self.drag_im_id)
            pygame.display.update()
            self.dragged = True
            self.prev_place = pos_drag

    def end_dragging(self):
        self.figure_dragging = False
        self.dragged = False





