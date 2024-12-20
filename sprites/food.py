import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, game_w, game_h, image_path_1, image_path_2):
        super().__init__()
        
        if random.randint(0, 100) < 95:
            self.image = pygame.image.load(image_path_1)
            size = 1
        else:
            self.image = pygame.image.load(image_path_2)
            size = 5

        self.rect = self.image.get_rect()
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_w = game_w
        self.game_h = game_h
        self.x = 0
        self.y = 0
        self.size = size
        self.change_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, head_x, head_y):
        self.rect.center = (self.x - head_x + self.screen_w / 2, self.y - head_y + self.screen_h / 2)

    def change_position(self):
        self.x = random.randint(10, self.game_w - 10)
        self.y = random.randint(10, self.game_h - 10)
