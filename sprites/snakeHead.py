import pygame
import random


class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, game_w, game_h,
                 image_path="assets/snake_fragment.png"):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_w / 2, screen_h / 2)
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_w = game_w
        self.game_h = game_h
        self.x = 0
        self.y = 0
        self.score = 0

    def get_is_alive(self, foods):
        if self.rect.left <= self.screen_w / 2 - self.x:
            return False
        if self.rect.top <= self.screen_h / 2 - self.y:
            return False
        if self.rect.right >= self.screen_w / 2 - self.x + self.game_w:
            return False
        if self.rect.bottom >= self.screen_h / 2 - self.y + self.game_h:
            return False
        
        for food in foods.sprites():
            if pygame.sprite.collide_rect(self, food):
                food.change_position()
                self.score += food.size

        return True

    def update(self, x, y):
        self.x = x
        self.y = y
