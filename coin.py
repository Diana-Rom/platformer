import pygame as pg
from screen_init import screen


class Coin:
    def __init__(self, x, y, radius, color) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self) -> None:
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)