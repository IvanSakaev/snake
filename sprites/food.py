import pygame
import random
import time


class Food(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, game_w, game_h, image_path="assets/food.png"):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_w = game_w
        self.game_h = game_h
        self.x = 0
        self.y = 0
        self.radius = self.rect.height / 2
        self.change_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, head_x, head_y):
        self.rect.center = (self.x - head_x + self.screen_w / 2, self.y - head_y + self.screen_h / 2)

    def change_position(self):
        self.x = random.randint(10, self.game_w - 10)
        self.y = random.randint(10, self.game_h - 10)
