import pygame
import sys

from sprites.snake import Snake



# Константы
WIDTH = 750
HEIGHT = 750
GAME_WIDTH = 1000
GAME_HEIGHT = 1000
FPS = 60
SNAKE_SIZE = 10



# Создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()



# Спрайты
snake = Snake(SNAKE_SIZE, screen_w=WIDTH, screen_h=HEIGHT,
              game_w=GAME_WIDTH, game_h=GAME_HEIGHT)



running = True
mouse_x = WIDTH / 2
mouse_y = HEIGHT / 2

while running:
    # Частота обновления экрана
    clock.tick(FPS)


    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]


    # Обновление спрайтов
    snake.update(mouse_x, mouse_y)
    head_x, head_y = snake.get_head_position()


    # Рендеринг
    screen.fill((255, 255, 255))
    snake.draw(screen)
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

    # Обновление экрана
    pygame.display.update()
