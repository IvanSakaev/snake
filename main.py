import pygame
import sys

from sprites.snake import Snake



# Константы
WIDTH = 500
HEIGHT = 500
FPS = 60
SNAKE_SIZE = 10



# Создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TVP")
clock = pygame.time.Clock()



# Спрайты
snake = Snake(SNAKE_SIZE)



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


    # Рендеринг
    screen.fill((255, 255, 255))
    snake.draw(screen)


    # Обновление спрайтов
    snake.update(mouse_x, mouse_y)


    # Обновление экрана
    pygame.display.update()
