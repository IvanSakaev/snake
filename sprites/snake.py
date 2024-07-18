import pygame
import vector


class Snake:
    def __init__(self, length, fragment_size=10, dot_size=2, screen_w=500,
                 screen_h=500, game_w=1000, game_h=1000,
                 image_path="assets/snake_fragment.png"):
        
        self.snake_list = [vector.obj(x = 10, y = 10)]
        self.length = length
        self.fragment_size = fragment_size
        self.dot_size = dot_size
        self.add_dots = (length - 1) * fragment_size

        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_w = game_w
        self.game_h = game_h

        self.image = pygame.image.load(image_path)
        
    def move(self, angle):
        v = vector.obj(rho=self.dot_size, phi=angle)
        self.snake_list.append(self.snake_list[-1] + v)
        if self.add_dots <= 0:
            self.snake_list.pop(0)
        else:
            self.add_dots -= 1
    
    def draw(self, surface):
        head_pos = self.get_head_position()
        head_v = vector.obj(x=head_pos[0], y=head_pos[1])
        for i in range((len(self.snake_list)-1) % self.fragment_size,
                       len(self.snake_list), self.fragment_size):
            draw_v = self.snake_list[i] - head_v
            rect = self.image.get_rect()
            rect.centerx = draw_v.x + self.screen_w / 2
            rect.centery = draw_v.y + self.screen_h / 2
            surface.blit(self.image, rect)

    def update(self, mouse_x, mouse_y):
        x = mouse_x - self.screen_w / 2
        y = mouse_y - self.screen_h / 2
        mouse_v = vector.obj(x=x, y=y)
        self.move(mouse_v.phi)

    def get_head_position(self):
        return (self.snake_list[-1].x, self.snake_list[-1].y)
