# Super class for all characters in the game

# Libraries
import pygame, math

# Character class
class Character(pygame.sprite.Sprite):
    hitpoints       = 100
    maxhitpoints    = 100
    speed           = 5
    angle           = 0     # Direction of looking (0-360)

    # Constructor
    def __init__(self, maxhitpoints, hitpoints, speed):
        pygame.sprite.Sprite.__init__(self)  # needed
        self.maxhitpoints   = maxhitpoints
        self.hitpoints      = hitpoints
        self.speed          = speed

    # Move the character in the direction she is looking (self.angle)
    def move_me(self):
        v = [math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180)]
        self.rect.x += v[0] * self.speed
        self.rect.y += v[1] * self.speed

    #
    def turn_right(self, increment):
        if self.angle+increment<360:
            self.angle+=increment
        else:
            self.angle=self.angle+increment-360

    def turn_left(self, increment):
        if self.angle-increment>0:
            self.angle-=increment
        else:
            self.angle=self.angle-increment+360
