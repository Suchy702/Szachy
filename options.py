import pygame
from save import is_disabled

class Options:
    def __init__(self, gui):
        self.choose_who_you_want_to_play_with = False
        self.choose_what_kind_of_game = True
        self.play_with_bot = False
        self.choose_new_game = True
        self.playing = True
        self.gui = gui

    def choose_with_play(self, pos_click):
        load_bot = is_disabled(True)
        load_player = is_disabled(False)
        self.gui.show_menu(load_bot, load_player)
        if 12 <= pos_click[0] <= 194 and 289 <= pos_click[1] <= 356:
            self.choose_new_game = True
            self.play_with_bot = False
            return True

        elif 402 <= pos_click[0] <= 584 and 293 <= pos_click[1] <= 360:
            self.choose_new_game = True
            self.play_with_bot = True
            return True

        elif 17 <= pos_click[0] <= 198 and 446 <= pos_click[1] <= 513 and load_player:
            self.choose_new_game = False
            self.play_with_bot = False
            return True

        elif 403 <= pos_click[0] <= 585 and 444 <= pos_click[1] <= 511 and load_bot:
            self.choose_new_game = False
            self.play_with_bot = True
            return True

    def choose_play_again(self, pos_click, winner):
        self.gui.won(winner)
        if 18 <= pos_click[0] <= 238 and 286 <= pos_click[1] <= 382:
            self.playing = True
            return True

        elif 373 <= pos_click[0] <= 593 and 287 <= pos_click[1] <= 383:
            quit()

    def showing(self, winner=None):
        clock = pygame.time.Clock()
        chosed = False
        while not chosed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if winner is not None:
                        chosed = self.choose_play_again(event.pos, winner)
                    else:
                        chosed = self.choose_with_play(event.pos)

            clock.tick(30)

    def reset(self):
        self.choose_who_you_want_to_play_with = False
        self.choose_what_kind_of_game = True
        self.play_with_bot = False
        self.choose_new_game = True
        self.playing = True

