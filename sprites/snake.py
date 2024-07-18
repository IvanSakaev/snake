import pygame
import vector


class Snake:
    def __init__(self, length, fragment_size=10, dot_size=2, image_path="assets/snake_fragment.png"):
        self.snake_list = [vector.obj(x = (i*dot_size) + 10, y = 10)
                           for i in range(length * fragment_size + 1)]
        self.length = length
        self.fragment_size = fragment_size
        self.dot_size = dot_size

        self.image = pygame.image.load(image_path)
        
    def move(self, angle, need_move_head):
        if need_move_head:
            v = vector.obj(rho=self.dot_size, phi=angle)
            self.snake_list.append(self.snake_list[-1] + v)
        else:
            self.snake_list.append(self.snake_list[-1])
        self.snake_list.pop(0)
    
    def draw(self, surface):
        for i in range(0, len(self.snake_list), self.fragment_size):
            rect = self.image.get_rect()
            rect.centerx = self.snake_list[i].x
            rect.centery = self.snake_list[i].y
            surface.blit(self.image, rect)

    def update(self, mouse_x, mouse_y):
        head_pos = self.get_head_position()
        head_v = vector.obj(x=head_pos[0], y=head_pos[1])
        mouse_v = vector.obj(x=mouse_x, y=mouse_y)
        head_to_mouse_v = mouse_v - head_v
        self.move(head_to_mouse_v.phi, head_to_mouse_v.rho >= self.dot_size)

    def get_head_position(self):
        return (self.snake_list[-1].x, self.snake_list[-1].y)
