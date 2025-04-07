import sys
import pygame

from constants import *
from sprites.resource_path import resource_path
from sprites.snake import Snake

snake1 = Snake(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT,
               SNAKE_SIZE, SNAKE_FRAGMENT_SIZE, SNAKE_DOT_SIZE,
               resource_path("assets/snake_fragment.png"))

snake2 = Snake(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT,
               SNAKE_SIZE, SNAKE_FRAGMENT_SIZE, SNAKE_DOT_SIZE,
               resource_path("assets/snake_fragment.png"))

player1_mouse_x = 0
player1_mouse_y = 0
player2_mouse_x = 0
player2_mouse_y = 0


def main(is_server):
    global player1_mouse_x, player1_mouse_y

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("server" if is_server else "client")
    clock = pygame.time.Clock()

    running = True

    while True:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                player1_mouse_x = event.pos[0]
                player1_mouse_y = event.pos[1]

        head_x, head_y = snake1.get_head_position()

        if is_server and (running or CHEATS):
            if not snake1.update(player1_mouse_x, player1_mouse_y, pygame.sprite.Group(), pygame.sprite.Group()):
                running = False
            if not snake2.update(player2_mouse_x, player2_mouse_y, pygame.sprite.Group(), pygame.sprite.Group()):
                running = False

        # Рендеринг
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0, 0, 0),
                         (WIDTH / 2 - head_x, HEIGHT / 2 - head_y),
                         (WIDTH / 2 - head_x + GAME_WIDTH, HEIGHT / 2 - head_y), 3)
        pygame.draw.line(screen, (0, 0, 0),
                         (WIDTH / 2 - head_x, HEIGHT / 2 - head_y + GAME_HEIGHT),
                         (WIDTH / 2 - head_x + GAME_WIDTH, HEIGHT / 2 - head_y + GAME_HEIGHT), 3)
        pygame.draw.line(screen, (0, 0, 0),
                         (WIDTH / 2 - head_x, HEIGHT / 2 - head_y),
                         (WIDTH / 2 - head_x, HEIGHT / 2 - head_y + GAME_HEIGHT), 3)
        pygame.draw.line(screen, (0, 0, 0),
                         (WIDTH / 2 - head_x + GAME_WIDTH, HEIGHT / 2 - head_y),
                         (WIDTH / 2 - head_x + GAME_WIDTH, HEIGHT / 2 - head_y + GAME_HEIGHT), 3)
        snake1.draw(screen)
        snake2.draw(screen, (head_x, head_y))
        pygame.display.update()


def get_movement1():
    return player1_mouse_x, player1_mouse_y


def set_movement2(x, y):
    global player2_mouse_x, player2_mouse_y
    player2_mouse_x = x
    player2_mouse_y = y
