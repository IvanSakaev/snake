import pygame
import random
import sys

from sprites.snake import Snake
from sprites.food import Food
from sprites.meteor import Meteor



# Константы
WIDTH = 750
HEIGHT = 750
GAME_WIDTH = 3000
GAME_HEIGHT = 3000
FPS = 60
SNAKE_SIZE = 10
FOOD_COUNT = 1000
METEOR_COUNT = 100
CHEATS = False



# Создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
pygame.font.init()
font1 = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 40)
clock = pygame.time.Clock()



# Спрайты
snake = Snake(screen_w=WIDTH, screen_h=HEIGHT,
              game_w=GAME_WIDTH, game_h=GAME_HEIGHT, length=SNAKE_SIZE)

foods = pygame.sprite.Group()
for i in range(FOOD_COUNT):
    foods.add(Food(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT))

meteors = pygame.sprite.Group()
for i in range(METEOR_COUNT):
    meteors.add(Meteor(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT))



running = True
mouse_x = WIDTH / 2
mouse_y = HEIGHT / 2
turbo = False

while True:
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if running == False:
                    snake = Snake(screen_w=WIDTH, screen_h=HEIGHT, game_w=GAME_WIDTH,
                                  game_h=GAME_HEIGHT, length=SNAKE_SIZE)
                    running = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            turbo = True
        if event.type == pygame.MOUSEBUTTONUP:
            turbo = False


    # Обновление спрайтов
    if running:
        if snake.update(mouse_x, mouse_y, foods):
            running = False
        if turbo and ((snake.get_score() > 0) or CHEATS):
            if snake.update(mouse_x, mouse_y, foods):
                running = False
            if not CHEATS:
                snake.turbo_reduce_score()
    head_x, head_y = snake.get_head_position()
    if running:
        if random.randint(0, 100) < 25:
            foods.add(Food(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT))
        foods.update(head_x, head_y)
        meteors.update(head_x, head_y)


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
    foods.draw(screen)
    meteors.draw(screen)
    snake.draw(screen)

    text = font2.render(f"score: {snake.get_score()}", False, (0, 0, 0))
    rect = text.get_rect()
    rect.top = 40
    rect.left = 40
    screen.blit(text, rect)

    if not running:
        text = font1.render("Game Over", False, (255, 0, 0))
        rect = text.get_rect()
        rect.center = (WIDTH / 2, HEIGHT / 6)
        screen.blit(text, rect)

    # Обновление экрана
    pygame.display.update()
