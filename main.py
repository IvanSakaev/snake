import pygame
import sys

from sprites.snake import Snake
from sprites.food import Food
from sprites.meteor import Meteor
from sprites.resource_path import resource_path



# Константы
WIDTH = 1000
HEIGHT = 750
GAME_WIDTH = 3000
GAME_HEIGHT = 3000
FPS = 60
SNAKE_SIZE = 5
SNAKE_FRAGMENT_SIZE = 10
SNAKE_DOT_SIZE = 2
FOOD_COUNT = 400
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
snake = Snake(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT,
              SNAKE_SIZE, SNAKE_FRAGMENT_SIZE, SNAKE_DOT_SIZE,
              resource_path("assets/snake_fragment.png"))

foods = pygame.sprite.Group()
for i in range(FOOD_COUNT):
    foods.add(Food(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT,
                   resource_path("assets/food.png"),
                   resource_path("assets/big_food.png")))

meteors = pygame.sprite.Group()
for i in range(METEOR_COUNT):
    meteors.add(Meteor(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT,
                       resource_path("assets/meteor.png")))



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
                    snake = Snake(WIDTH, HEIGHT, GAME_WIDTH, GAME_HEIGHT,
                                  SNAKE_SIZE, SNAKE_FRAGMENT_SIZE,
                                  SNAKE_DOT_SIZE,
                                  resource_path("assets/snake_fragment.png"))
                    for meteor in meteors.sprites():
                        meteor.move_to_start_position()
                    for food in foods.sprites():
                        food.change_position()
                    running = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            turbo = True
        if event.type == pygame.MOUSEBUTTONUP:
            turbo = False


    # Обновление спрайтов
    if running or CHEATS:
        meteors.update()
        if not snake.update(mouse_x, mouse_y, foods, meteors):
            running = False
        if turbo and ((snake.get_score() > 0) or CHEATS):
            if not snake.update(mouse_x, mouse_y, foods, meteors):
                running = False
            if not CHEATS:
                snake.turbo_reduce_score()
    head_x, head_y = snake.get_head_position()
    if running or CHEATS:
        foods.update(head_x, head_y)


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

    if not running and not CHEATS:
        text = font1.render("Game Over", False, (255, 0, 0))
        rect = text.get_rect()
        rect.center = (WIDTH // 2, HEIGHT // 6)
        screen.blit(text, rect)

    # Обновление экрана
    pygame.display.update()
