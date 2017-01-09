# Super class for all characters in the game

# Libraries
import math
import pygame
import funcs
import class_projectile


# Character class
class Character(pygame.sprite.Sprite):

    angle           = 0

    # Constructor
    def __init__(self,):
        pass

    # Move the character in the direction she is looking (self.angle)
    def move(self):
        v = (math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180))
        self.rect.x += v[0] * self.speed
        self.rect.y += v[1] * self.speed

    # Rotate the character to the left or right side
    def turn(self, increment, direction):
        # Set the character's angle into the right direction
        if direction == "right":
            if self.angle+increment<360:
             self.angle+=increment
            else:
             self.angle=self.angle+increment-360
        else:
            if self.angle - increment > 0:
                self.angle -= increment
            else:
                self.angle = self.angle - increment + 360
        # Rotate the characters image into the right direction
        self.update_img()

    # Update the image, when character rotates
    def update_img(self):
        self.image = pygame.transform.rotate(
                self.base_img, -(self.angle))
