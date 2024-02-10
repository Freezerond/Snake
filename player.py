import sys
from settings import *
from random import randrange
import pygame as pg

class Player:
    def __init__(self, game):
        pg.font.init()
        self.dirs = {'W': True, 'S': True, 'A': True, 'D': True, 'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
        self.game = game
        self.x, self.y = players_pos
        self.snake = [(self.x, self.y)]
        self.length = 1
        self.dx, self.dy = 0, 0
        self.apple = self.food_x, self.food_y = round(randrange(SIZE, WIDTH - SIZE, SIZE)), round(randrange(SIZE, HEIGHT - SIZE, SIZE))

    def chek_game_over(self):
        my_font = pg.font.SysFont('Comic Sans MS', SIZE)
        msg = my_font.render('YOU LOSE', True, 'white')
        if self.x >= WIDTH / SIZE - 1 or self.x < 1 or self.y >= HEIGHT / SIZE - 1 or self.y < 1 or len(self.snake) != len(set(self.snake)):
            while True:
                self.game.screen.blit(msg, [WIDTH / 2 - 100, HEIGHT / 2 - 20])
                pg.display.flip()
                self.game.check_events()


    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            if self.dirs['W'] or self.dirs['UP']:
                self.dy = -1
                self.dx = 0
                self.dirs = {'W': True, 'S': False, 'A': True, 'D': True, 'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            if self.dirs['D'] or self.dirs['RIGHT']:
                self.dx = 1
                self.dy = 0
                self.dirs = {'W': True, 'S': True, 'A': False, 'D': True, 'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            if self.dirs['S'] or self.dirs['DOWN']:
                self.dx = 0
                self.dy = 1
                self.dirs = {'W': False, 'S': True, 'A': True, 'D': True, 'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            if self.dirs['A'] or self.dirs['LEFT']:
                self.dy = 0
                self.dx = -1
                self.dirs = {'W': True, 'S': True, 'A': True, 'D': False, 'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}

        self.x += self.dx
        self.y += self.dy

        if self.snake[-1] == (self.food_x/SIZE, self.food_y/40):
            self.apple = self.food_x, self.food_y = round(randrange(SIZE, WIDTH - SIZE, SIZE)), round(randrange(SIZE, HEIGHT - SIZE, SIZE))
            self.length += 1
        self.snake.append((self.x, self.y))
        self.snake = self.snake[-self.length:]

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', (*self.apple, SIZE, SIZE))
        [pg.draw.rect(self.game.screen, 'green', (i * SIZE, j * SIZE, SIZE - 1, SIZE - 1)) for i, j in self.snake]

    def update(self):
        self.movement()
        self.chek_game_over()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)