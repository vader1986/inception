#---------------------------------------------------------+
# React to user input (keyboard/joystick)
#---------------------------------------------------------+
import pygame
import Constants

def listen(event, lvl):
    # Key Pressed events
    if event.type == pygame.KEYDOWN:
        if event.key == Constants.left:
            lvl.player.position[0]-=1
        if event.key == Constants.right:
            lvl.player.position[0] += 1
        if event.key == Constants.up:
            lvl.player.position[1]-=1
        if event.key == Constants.down:
            lvl.player.position[1]+=1
