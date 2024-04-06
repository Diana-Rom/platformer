import pygame as pg
from character import Character
from screen_init import screen
from block import Block
import constants
import block

blocks = [
    Block(x=100, y=230, size=[60, 60],color=(124, 190, 210)),
    Block(x=165, y=190, size=[60, 100],color=(124, 190, 210)),
    Block(x=165, y=10, size=[60, 60],color=(124, 190, 210))

]
char1 = Character(x=100, y=100, size=[20, 40], speed=3, hp=100)
font = pg.font.Font(None, 36)

clock = pg.time.Clock()
FPS = 30

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.KEYDOWN:

    keys = pg.key.get_pressed()
    for block in blocks:
        if keys[pg.K_LEFT] == True:
            char1.move("left")
            char1.bound()
            print(char1.check_collision(block))
            if char1.y > block.y:
                while char1.check_collision(block):
                    char1.move('right')
        if keys[pg.K_RIGHT] == True:
            # char1.jumping = False #?
            char1.move('right')
            char1.bound()
            if char1.y > block.y:
                while char1.check_collision(block):
                    char1.move('left')
        if keys[pg.K_UP] == True and char1.jumping == False:
            char1.jump()
            # char1.y -= 1
        # if keys[pg.K_DOWN] == True:
            # char1.y += 1
        if char1.jumping == True:
            char1.y -= char1.boost
            char1.boost -= 1
            if char1.y >= 250:
                char1.y = 250
                char1.jumping = False
                char1.boost = constants.BOOST 
                char1.falling = False
            if char1.check_collision(block) and char1.falling and char1.y < block.y:
                char1.jumping = False
                char1.boost = constants.BOOST
                char1.falling = False
                while char1.check_collision(block):
                    char1.y -= 1
                char1.y += 1

            if char1.check_collision(block) and char1.jumping and char1.y > block.y:
                char1.boost = 0
                while char1.check_collision(block):
                    char1.y += 1


        if char1.y < 250 and char1.jumping == False and not char1.check_collision(block):
            if char1.falling == False:
                char1.falling = True
                char1.jumping = True
                char1.boost = 0

        if char1.boost < 0:
            char1.falling = True
          
        block.draw()
    text = font.render(f"{char1.x} {char1.y}", True, (255,255,255))
    screen.blit(text, (20,20))
        

    char1.draw()
    # print(char1.check_collision(block))
    pg.display.flip()
    clock.tick(FPS)
    # print(char1.boost, char1.falling, char1.jumping)
