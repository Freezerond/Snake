import pygame
from random import randrange

# Константы
RES, SIZE = 800, 50
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)

# Инициализация
pygame.init()
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
move_delay = 10  # Задержка движения змейки
move_counter = 0

def close_game():
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        exit()

def draw_text(text, size, pos, color=WHITE):
    font = pygame.font.SysFont('Arial', size, bold=True)
    render = font.render(text, True, color)
    screen.blit(render, pos)

def show_start_screen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        screen.fill(BLACK)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (RES / 2, RES / 2)
        screen.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (RES / 2, RES / 2)
        screen.blit(rotatedSurf2, rotatedRect2)

        draw_text('Press any key to play.', 30, (RES / 3, RES - 50))

        if pygame.event.get(pygame.KEYUP):
            return
        close_game()
        pygame.display.update()
        clock.tick(30)
        degrees1 += 3
        degrees2 += 7

def show_game_over_screen():
    while True:
        screen.fill(BLACK)
        draw_text('GAME OVER', 80, (RES // 4, RES // 3))
        draw_text('Press any key to restart', 40, (RES // 4, RES // 2))
        pygame.display.flip()
        if pygame.event.get(pygame.KEYUP):
            return
        close_game()

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
while apple == (x, y):
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
snake = [(x, y)]
dx, dy, length, score = 0, 0, 1, 0

def reset_game():
    global x, y, apple, snake, dx, dy, length, score
    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    while apple == (x, y):
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    snake, dx, dy, length, score = [(x, y)], 0, 0, 1, 0

show_start_screen()
waiting_for_input = False
while True:
    screen.fill(BLACK)
    close_game()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and dy == 0: dx, dy, waiting_for_input = 0, -1, True
    if keys[pygame.K_s] and dy == 0: dx, dy, waiting_for_input = 0, 1, True
    if keys[pygame.K_a] and dx == 0: dx, dy, waiting_for_input = -1, 0, True
    if keys[pygame.K_d] and dx == 0: dx, dy, waiting_for_input = 1, 0, True

    move_counter += 1
    if move_counter >= move_delay:
        move_counter = 0
        if waiting_for_input:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        while apple in snake:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1

    if x < 0 or x >= RES or y < 0 or y >= RES or len(snake) != len(set(snake)):
        waiting_for_input = False
        show_game_over_screen()
        reset_game()

    [pygame.draw.rect(screen, GREEN, (i, j, SIZE - 2, SIZE - 2)) for i, j in snake]
    pygame.draw.rect(screen, RED, (*apple, SIZE-2, SIZE-2))
    draw_text(f'Score: {score}', 30, (10, 10), WHITE)

    pygame.display.update()
    clock.tick(FPS)

