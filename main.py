from GUI import GUI
from game import Game
from options import Options


def main():
    gui = GUI()
    options = Options(gui)
    while options.playing:
        options.showing()
        game = Game(options.play_with_bot, options.choose_new_game, gui)
        winner = game.play()
        options.showing(winner)
        print(options.playing)


if __name__ == "__main__":
    main()
