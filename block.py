import pygame as pg
from screen_init import screen


class Block:
    def __init__(self, x, y, size, color) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
    def draw(self) -> None:
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size[0], self.size[1]))

    
    