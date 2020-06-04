from Board import Board
from Engine import Engine
from events import Events
from bot import Bot
from save import end_with_save
from save import update
import pygame


class Game:
    def __init__(self, play_with_bot, new_game, gui):
        self.events = Events()
        self.board = Board()
        self.engine = Engine()
        self.bot = Bot()
        self.gui = gui

        self.play_wiht_bot = play_with_bot
        self.someone_win = False

        if not new_game:
            self.engine, self.board.board = update(play_with_bot)

    def player_move(self, pos_click, animation):
        self.events.what_to_do(self.events.where_clik(pos_click), self.gui, self.engine, self.board.board, animation)
        self.someone_win = self.engine.is_end(self.board.board)
        self.gui.update_screen()
        if self.someone_win:
            self.gui.won(self.engine.win)

    def bot_move(self):
        self.bot.move(self.engine, self.gui, self.board)
        self.gui.show_board(self.board.board)
        self.someone_win = self.engine.is_end(self.board.board)
        self.gui.update_screen()
        if self.someone_win:
            self.gui.won(self.engine.win)

    def move_with_bot(self, pos_click, animation):
        self.player_move(pos_click, animation)
        if not self.someone_win and self.engine.which_tour() == -1:
            self.bot_move()

    def play(self):
        clock = pygame.time.Clock()
        while not self.someone_win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_with_save(self.engine, self.play_wiht_bot, self.board.board)

                if event.type == pygame.MOUSEBUTTONUP:
                    self.events.end_dragging()
                    if self.play_wiht_bot:
                        self.move_with_bot(event.pos, False)
                    else:
                        self.player_move(event.pos, False)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = pygame.mouse.get_pos()
                    self.events.pre_drag(pos_click, self.gui, self.engine, self.board.board)
                    if self.play_wiht_bot:
                        self.move_with_bot(pos_click, True)
                    else:
                        self.player_move(pos_click, True)

                elif event.type == pygame.MOUSEMOTION:
                    if self.events.figure_dragging:
                        self.events.dragging(event.pos, self.gui, self.board.board)

            clock.tick(60)

        return self.engine.win