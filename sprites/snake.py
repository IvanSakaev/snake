import pygame
import vector

from sprites.snakeHead import SnakeHead


class Snake:
    def __init__(self, screen_w, screen_h, game_w, game_h,
                 length, fragment_size=10, dot_size=2,
                 image_path="assets/snake_fragment.png"):
        
        self.snake_list = [vector.obj(x = game_w / 2, y = game_h / 2)]
        self.start_length = length
        self.length = length
        self.fragment_size = fragment_size
        self.dot_size = dot_size
        self.add_dots = (length - 1) * fragment_size

        self.screen_w = screen_w
        self.screen_h = screen_h
        self.game_w = game_w
        self.game_h = game_h

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.head = SnakeHead(self.screen_w, self.screen_h,
                              self.game_w, self.game_h, image_path)
        self.radius = self.rect.height / 2
        
        self.turbo_timer = 0
        
    def move(self, angle):
        v = vector.obj(rho=self.dot_size, phi=angle)
        self.snake_list.append(self.snake_list[-1] + v)
        if self.add_dots <= 0:
            self.snake_list.pop(0)
        else:
            self.add_dots -= 1
        self.head.update(self.snake_list[-1].x, self.snake_list[-1].y)
        length = self.start_length + self.head.score // 10
        if length < self.length:
            for i in range((self.length - length) * self.fragment_size):
                self.snake_list.pop(0)
            self.length = length
        elif length > self.length:
            self.add_dots += (length - self.length) * self.fragment_size
            self.length = length
    
    def draw(self, surface):
        head_pos = self.get_head_position()
        head_v = vector.obj(x=head_pos[0], y=head_pos[1])
        for i in range((len(self.snake_list)-1) % self.fragment_size,
                       len(self.snake_list), self.fragment_size):
            draw_v = self.snake_list[i] - head_v
            self.rect.centerx = draw_v.x + self.screen_w / 2
            self.rect.centery = draw_v.y + self.screen_h / 2
            surface.blit(self.image, self.rect)

    def update(self, mouse_x, mouse_y, foods, meteors):
        x = mouse_x - self.screen_w / 2
        y = mouse_y - self.screen_h / 2
        mouse_v = vector.obj(x=x, y=y)
        self.move(mouse_v.phi)

        head_pos = self.get_head_position()
        for meteor in meteors.sprites():
            meteor.update_rect(head_pos[0], head_pos[1])

        good = True
        head_v = vector.obj(x=head_pos[0], y=head_pos[1])
        for i in range((len(self.snake_list)-1) % self.fragment_size,
                       len(self.snake_list), self.fragment_size):
            draw_v = self.snake_list[i] - head_v
            self.rect.centerx = draw_v.x + self.screen_w / 2
            self.rect.centery = draw_v.y + self.screen_h / 2
            for meteor in meteors.sprites():
                if pygame.sprite.collide_rect(self, meteor):
                    if pygame.sprite.collide_circle(self, meteor):
                        good = False

        if not self.head.get_is_alive(foods):
            good = False

        return good
    
    def turbo_reduce_score(self):
        self.turbo_timer += 1
        if self.turbo_timer >= 5:
            self.head.score -= 1
            self.turbo_timer = 0

    def get_score(self):
        return self.head.score

    def get_head_position(self):
        return (self.snake_list[-1].x, self.snake_list[-1].y)
