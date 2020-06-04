import Board
import shelve
from tkinter import messagebox
import tkinter as tk
import os


def save(engine, save_bot, board):
    cwd = os.getcwd()
    path = os.path.join(cwd, 'mydata')
    shelf_file = shelve.open(path)
    if save_bot:
        shelf_file['bot_board'] = board
        shelf_file['bot_engine'] = engine
    else:
        shelf_file['player_board'] = board
        shelf_file['player_engine'] = engine
    shelf_file.close()


def update(update_bot):
    cwd = os.getcwd()
    path = os.path.join(cwd, 'mydata')
    shelf_file = shelve.open(path)
    if update_bot:
        board = shelf_file['bot_board']
        r_engine = shelf_file['bot_engine']
    else:
        board = shelf_file['player_board']
        r_engine = shelf_file['player_engine']
    shelf_file.close()
    return r_engine, board


def end_with_save(engine, play_with_bot, board):
    root = tk.Tk()
    root.overrideredirect(1)  # <-To może być, choć nie musi (coś wspominali o miganiu) u mnie bez tego nie miga.
    root.withdraw()
    if messagebox.askokcancel("Uwaga !", "Czy chcesz zapisać grę ?"):
        save(engine, play_with_bot, board)
    quit()


def is_disabled(bot_checking):
    example = Board.Board()
    cwd = os.getcwd()
    path = os.path.join(cwd, 'mydata')
    shelf_file = shelve.open(path)
    if bot_checking:
        try:
            return shelf_file['bot_board'] != example
        except:
            return False
    else:
        try:
            return shelf_file['player_board'] != example
        except:
            return False