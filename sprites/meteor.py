import pygame
import vector
import random
import math


class Meteor(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, game_w, game_h):
        super().__init__()
        self.image = pygame.image.load("assets/big_food.png")
        self.rect = self.image.get_rect()
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_w = game_w
        self.game_h = game_h
        self.radius = self.rect.height / 2
        self.x = 0
        self.y = 0
        self.move_x = 0
        self.move_y = 0
        self.move_to_start_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.x += self.move_x
        self.y += self.move_y
        if self.x < 0:
            self.x = self.game_w - self.rect.width
        if self.y < 0:
            self.y = self.game_h - self.rect.height
        if self.x > self.game_w:
            self.x = self.rect.width
        if self.y > self.game_h:
            self.y = self.rect.height
        
    def update_rect(self, head_x, head_y):
        self.rect.center = (self.x - head_x + self.screen_w / 2,
                            self.y - head_y + self.screen_h / 2)
        
    def move_to_start_position(self):
        self.x = self.game_w / 2
        self.y = self.game_h / 2

        offset = 500
        n = random.randint(0, self.game_w + 
                           (self.game_h - offset * 2))
        m = random.randint(0, offset * 2)
        if n <= self.game_w:
            self.x = n
            if m <= offset:
                self.y = m
            else:
                self.y = self.game_h - (m - offset)
        else:
            self.y = n + offset - self.game_w
            if m <= offset:
                self.x = m
            else:
                self.x = self.game_w - (m - offset)

        phi = random.uniform(0, math.pi * 2)
        rho = random.uniform(1, 2)
        move_v = vector.obj(phi=phi, rho=rho)
        self.move_x = move_v.x
        self.move_y = move_v.y
