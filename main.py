import pygame as pg
from character import Character
from screen_init import screen
from block import Block

block = Block(x=100, y=250, size=[60, 60],color=(124, 190, 210))
char1 = Character(x=50, y=250, size=[20, 40], speed=5, hp=100)

clock = pg.time.Clock()
FPS = 60

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.KEYDOWN:

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] == True:
        char1.move("left")
        char1.bound()
        if char1.check_collision(block):
            char1.move('right')
    if keys[pg.K_RIGHT] == True:
        char1.jumping = False
        char1.move('right')
        char1.bound()
        if char1.check_collision(block):
            char1.move('left')
    if keys[pg.K_UP] == True and char1.jumping == False:
        char1.jump()
        # char1.y -= 1
    if keys[pg.K_DOWN] == True:
        char1.y += 1
    if char1.jumping == True:
        char1.y -= char1.boost
        char1.boost -= 1
        if char1.y >= 250:
            char1.y = 250
            char1.jumping = False
            char1.boost = 10 
            char1.falling = False
        if char1.check_collision(block) and char1.falling:
            char1.jumping = False
            char1.boost = 10
            char1.falling = False

    if char1.y < 250 and char1.jumping == False:
        if char1.falling == False:
            char1.falling = True
            char1.jumping = True
            char1.boost = 0



    if char1.boost < 0:
        char1.falling = True
     
    
    # print(keys)
    # square = pg.draw.rect(56, 38, 20, 20, (255, 0, 0))
    # screen.blit(square, (45, 83))
    # pg.draw.rect(screen, (255, 0, 0), (56, 38, 20, 20))
    char1.draw()
    block.draw()
    print(char1.check_collision(block))
    pg.display.flip()
    clock.tick(FPS)
    print(char1.boost, char1.falling, char1.jumping)

