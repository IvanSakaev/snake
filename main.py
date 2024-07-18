import pygame
import sys


# Константы
WIDTH = 500
HEIGHT = 500
FPS = 60



# Создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TVP")
clock = pygame.time.Clock()



# Спрайты



running = True
while running:
    # Частота обновления экрана
    clock.tick(FPS)


    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Рендеринг
    screen.fill((255, 255, 255))


    # Обновление спрайтов


    # Обновление экрана
    pygame.display.update()
