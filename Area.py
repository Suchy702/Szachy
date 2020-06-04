class Area:
    def __init__(self, posx, posy, background, checker=None):
        self.posx = posx
        self.posy = posy
        self.checker = checker
        self.background = background


    def bg_color(self):
        if self.background == 'W':
            return 1
        else:
            return 2
