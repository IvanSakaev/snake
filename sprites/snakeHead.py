import pygame


class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, game_width=1000, game_height=1000,
                 image_path="assets/snake_fragment.png"):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.game_width = game_width
        self.game_height = game_height

    def get_in_wall(self):
        if self.rect.left <= 0:
            return True
        elif self.rect.top <= 0:
            return True
        elif self.rect.right >= self.game_width:
            return True
        elif self.rect.bottom >= self.game_height:
            return True
        else:
            return False

    def update(self, x, y):
        self.rect.center = (x, y)
