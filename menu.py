import pygame_menu

class Menu:
    def __init__(self, game):
        self.game = game

    #@classmethod
    def set_difficulty(self):
        pass

    #@classmethod
    def start_the_game(self):
        pass

    def show_menu(self):
        self.menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.selector('Difficulty :', [('Easy', 1), ('Normal', 2), ('Hard', 3)], onchange = self.set_difficulty())
        self.menu.add.button('Play', self.start_the_game())
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        self.menu.mainloop(self.game.screen)