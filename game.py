'''
Main game file
author: basti hoffmeister
'''

import sys, pygame, os

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "imgs/hero.png"
abs_file_path = os.path.join(script_dir, rel_path)

ball = pygame.image.load(abs_file_path)
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()