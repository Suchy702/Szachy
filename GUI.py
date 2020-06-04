import pygame
import os
from save import is_disabled
pygame.init()


class GUI:
    def __init__(self):
        self.project_path = os.path.join(os.path.dirname(__file__), "images")
        self.board_img = pygame.image.load(os.path.join(self.project_path, "board.png"))
        self.figures_images = self.load_figures_images()
        self.bg_images = self.load_bg_images()
        self.screen_images = self.load_screen_images()
        self.screen = pygame.display.set_mode((600, 600))
        self.show_menu(is_disabled(True), is_disabled(False))
        pygame.display.update()

    def show_board(self, board):
        self.screen.blit(self.board_img, (0, 0))
        for row in board:
            for area in row:
                if area.checker is not None:
                    self.screen.blit(self.figures_images[area.checker.image_id], (area.posx, area.posy))

    def load_figures_images(self):
        figures_images = []
        fig = ['_king.png', '_queen.png', '_rook.png', '_knight.png', '_bishop.png', '_pawn.png']
        for checker in fig:
            for color in 'BW':
                figures_images.append(pygame.image.load(os.path.join(self.project_path, color + checker)))
                figures_images.append('dummy')

        return figures_images

    def load_bg_images(self):
        bg_names = ["gray_circle.png", "W_background.png", "B_background.png"]
        bg_images = []
        for image_name in bg_names:
            bg_images.append(pygame.image.load(os.path.join(self.project_path, image_name)))
        return bg_images

    def load_screen_images(self):
        image_names = ["menu.png", "W_win.png", "B_win.png", "classic.png", "disabled_button.png"]
        screen_images = []
        for image_name in image_names:
            screen_images.append(pygame.image.load(os.path.join(self.project_path, image_name)))
        return screen_images

    def show_menu(self, disabled_bot, disabled_player):
        self.screen.blit(self.screen_images[3], (221, 316))
        self.screen.blit(self.screen_images[0], (0, 0))
        if not disabled_bot:
            self.screen.blit(self.screen_images[4], (403, 444))
        if not disabled_player:
            self.screen.blit(self.screen_images[4], (17, 446))
        pygame.display.update()

    def won(self, color):
        if color == 1:
            self.screen.blit(self.screen_images[1], (0, 0))
        else:
            self.screen.blit(self.screen_images[2], (0, 0))
        pygame.display.update()

    def show_figure(self, pos, image_id):
        self.screen.blit(self.figures_images[image_id], pos)

    def what_must_update(self, pos, board, size):
        upd_areas = []
        vertices = [(pos[0], pos[1]), (pos[0] + 75, pos[1]), (pos[0], pos[1] + 75), (pos[0] + 75, pos[1] + 75)]
        if size == 'big':
            add_vertices = [(pos[0] + 37.5, pos[1] - 37.5), (pos[0] + 37.5, pos[1] + 37.5 + 75),
                            (pos[0] - 37.5, pos[1] + 37.5), (pos[0] + 37.5 + 75, pos[1] - 37.5)]
            vertices += add_vertices
        for row in range(8):
            for column in range(8):
                for ver in vertices:
                    area = board[row][column]
                    if area.posx <= ver[0] <= area.posx + 75 and area.posy <= ver[1] <= area.posy + 75:
                        upd_areas.append((row, column))
        return upd_areas

    def show_possible_moves(self, positions, board):
        for pos in positions:
            area = board[pos[0]][pos[1]]
            self.screen.blit(self.bg_images[0], (area.posx, area.posy))

    def update(self, positions, board):
        for pos in positions:
            area = board[pos[0]][pos[1]]
            self.screen.blit(self.bg_images[area.bg_color()], (area.posx, area.posy))
            if area.checker is not None:
                self.screen.blit(self.figures_images[area.checker.create_image_id()], (area.posx, area.posy))

    def normal_animation(self, start_pos, new_pos, board):
        addx = (new_pos.posx - start_pos.posx) / 60
        addy = (new_pos.posy - start_pos.posy) / 60
        x, y = start_pos.posx, start_pos.posy
        clock = pygame.time.Clock()
        self.show_board(board)
        while new_pos.posy + addy != y or new_pos.posx + addx != x:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.update(self.what_must_update((x, y), board, 'small'), board)
            self.screen.blit(self.bg_images[start_pos.bg_color()], (start_pos.posx, start_pos.posy))
            self.show_figure((x, y), start_pos.checker.create_image_id())
            pygame.display.update()
            x += addx
            y += addy
            clock.tick(120)

    def castling_animation(self, start_pos, new_pos, board):
        k_addx = (new_pos.posx - start_pos.posx) / 60
        k_x, k_y = start_pos.posx, start_pos.posy
        if new_pos.posy == 0:
            r_y = 0
            bg_color = [1, 2]
        else:
            bg_color = [2, 1]
            r_y = 525

        if new_pos.posx == 150:
            bg_id = 0
            bg_x = r_x = 0
            r_addx = (150 - 0) / 40
        else:
            bg_id = 1
            bg_x = r_x = 525
            r_addx = (450 - 525) / 30

        clock = pygame.time.Clock()
        self.show_board(board)
        while new_pos.posx + k_addx != k_x:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.update(self.what_must_update((r_x, r_y), board, 'small'), board)
            self.update(self.what_must_update((k_x, k_y), board, 'small'), board)
            self.screen.blit(self.bg_images[start_pos.bg_color()], (start_pos.posx, start_pos.posy))
            self.screen.blit(self.bg_images[bg_color[bg_id]], (bg_x, r_y))
            self.show_figure((r_x, r_y), start_pos.checker.color + 9)
            self.show_figure((k_x, k_y), start_pos.checker.create_image_id())
            pygame.display.update()
            k_x += k_addx
            r_x += r_addx
            clock.tick(120)

    def kind_of_animation(self, start_pos, new_pos, kind_of_animation, board):
        if kind_of_animation == 'Castling':
            self.castling_animation(start_pos, new_pos, board)
        else:
            self.normal_animation(start_pos, new_pos, board)

    def update_screen(self):
        pygame.display.update()