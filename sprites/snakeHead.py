import pygame


class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, game_width, game_height,
                 image_path="assets/snake_fragment.png"):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_w / 2, screen_h / 2)
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_width = game_width
        self.game_height = game_height
        self.radius = self.rect.height / 2
        self.x = 0
        self.y = 0

    def get_in_wall(self, foods : pygame.sprite.Group):
        if self.rect.left <= self.screen_w / 2 - self.x:
            return True
        if self.rect.top <= self.screen_h / 2 - self.y:
            return True
        if self.rect.right >= self.screen_w / 2 - self.x + self.game_width:
            return True
        if self.rect.bottom >= self.screen_h / 2 - self.y + self.game_height:
            return True
        
        for food in foods.sprites():
            if pygame.sprite.collide_circle(self, food):
                food.change_position()

        return False

    def update(self, x, y):
        self.x = x
        self.y = y