import pygame
import vector
from time import sleep

from sprites.snakeHead import SnakeHead


class Snake:
    def __init__(self, screen_w, screen_h, game_w, game_h,
                 length, fragment_size, dot_size,
                 image_path):

        self._lock = False
        self.snake_list = [vector.obj(x=game_w / 2, y=game_h / 2)]
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

    def calk_length(self, ignore_lock=False):
        if not ignore_lock:
            while self._lock:
                sleep(0.01)
            self._lock = True
        length = self.start_length + self.head.score // 10
        if length < self.length:
            for i in range((self.length - length) * self.fragment_size):
                self.snake_list.pop(0)
            self.length = length
        elif length > self.length:
            self.add_dots += (length - self.length) * self.fragment_size
            self.length = length
        if not ignore_lock:
            self._lock = False

    def move(self, angle, ignore_lock=False):
        if not ignore_lock:
            while self._lock:
                sleep(0.01)
            self._lock = True
        v = vector.obj(rho=self.dot_size, phi=angle)
        self.snake_list.append(self.snake_list[-1] + v)
        if self.add_dots <= 0:
            self.snake_list.pop(0)
        else:
            self.add_dots -= 1
        self.head.update(self.snake_list[-1].x, self.snake_list[-1].y)
        self.calk_length(True)
        if not ignore_lock:
            self._lock = False

    def move_head(self, x, y):
        while self._lock:
            sleep(0.01)
        self._lock = True
        self.snake_list.append(vector.obj(x=x, y=y))
        if self.add_dots <= 0:
            self.snake_list.pop(0)
        else:
            self.add_dots -= 1
        self.head.update(x, y)
        self.calk_length(True)
        self._lock = False

    def draw(self, surface, head_pos=None):
        while self._lock:
            sleep(0.01)
        self._lock = True
        if head_pos is None:
            head_pos = self.get_head_position()
        head_v = vector.obj(x=head_pos[0], y=head_pos[1])
        for i in range((len(self.snake_list) - 1) % self.fragment_size,
                       len(self.snake_list), self.fragment_size):
            draw_v = self.snake_list[i] - head_v
            self.rect.centerx = draw_v.x + self.screen_w / 2
            self.rect.centery = draw_v.y + self.screen_h / 2
            surface.blit(self.image, self.rect)
        self._lock = False

    def update(self, mouse_x, mouse_y, foods, meteors, optimized=False):
        while self._lock:
            sleep(0.01)
        self._lock = True
        if optimized:
            x = mouse_x
            y = mouse_y
        else:
            x = mouse_x - self.screen_w / 2
            y = mouse_y - self.screen_h / 2
        if x == 0 and y == 0:
            return True
        mouse_v = vector.obj(x=x, y=y)
        self.move(mouse_v.phi, True)

        head_pos = self.get_head_position()
        for meteor in meteors.sprites():
            meteor.update_rect(head_pos[0], head_pos[1])

        good = True
        head_v = vector.obj(x=head_pos[0], y=head_pos[1])
        for i in range((len(self.snake_list) - 1) % self.fragment_size,
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
        self._lock = False

        return good

    def turbo_reduce_score(self):
        while self._lock:
            sleep(0.01)
        self._lock = True
        self.turbo_timer += 1
        if self.turbo_timer >= 5:
            self.head.score -= 1
            self.turbo_timer = 0
        self._lock = False

    def get_score(self):
        return self.head.score

    def get_head_position(self):
        return self.snake_list[-1].x, self.snake_list[-1].y

    def serialize(self):
        while self._lock:
            sleep(0.01)
        self._lock = True
        segments = []
        for segment in self.snake_list:
            segments.append(str(int(segment.x)) + "," + str(int(segment.y)))
        out = " ".join(segments)
        self._lock = False
        return out

    def load(self, serialized):
        while self._lock:
            sleep(0.01)
        self._lock = True
        self.snake_list.clear()
        segments = serialized.split(" ")
        for segment in segments:
            segment = list(map(int, segment.split(",") ))
            self.snake_list.append(vector.obj(x=segment[0], y=segment[1]))
        self._lock = False
