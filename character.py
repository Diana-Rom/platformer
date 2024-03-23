import pygame as pg
from screen_init import screen

class Character:
    def __init__(self, x, y, size, speed, hp ) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.hp = hp
        self.boost = 10
        self.jumping = False
        self.falling = False

    def draw(self) -> None:
        pg.draw.rect(screen, (123, 104, 238), (self.x, self.y, self.size[0], self.size[1]))
    
    def move(self, direction) -> None:
        if direction == 'left':
            self.x -= self.speed
        if direction == 'right':
            self.x += self.speed
        if direction == 'up':
            self.y -= self.speed
        if direction == 'down':
            self.y += self.speed

    def bound(self) -> None:
        if self.x < 0:
            self.x = 0
        if self.x > 1000 - self.size[0]: # формула: ширина экрана - ширина персонажа
            self.x = 1000 - self.size[0]


    def check_collision(self, obj) -> bool:
        return self.x + self.size[0] > obj.x and self.y + self.size[1] > obj.y and self.x < obj.x + obj.size[0] and self.y < obj.y + obj.size[1]

    def check_multiple_collision(self, objects) -> bool:
        for object in objects:
            if self.check_collision(object):
                return True
        return False

    def jump(self) -> None:
        self.jumping = True

    

class Player(Character):
    def __init__(self, x, y,size, speed, hp, name) -> None:
        super().__init__(y=y, x=x, size=size, speed=speed, hp=hp)
        self.name = name