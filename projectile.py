# Projectiles are fired by characters

import pygame, funcs, math

class Projectile(pygame.sprite.Sprite):

    def __init__(self, rel_path_img, x, y, angle, speed, dmg):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.image      = funcs.load_img(rel_path_img)
        self.base_img   = self.image
        self.rect       = self.image.get_rect()
        self.dmg        = dmg
        self.rect.x     = x
        self.rect.y     = y
        self.angle      = angle
        self.speed      = speed
        self.update_img()

    # Move the projectile
    def move(self):
        v = [math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180)]
        self.rect.x += v[0] * self.speed
        self.rect.y += v[1] * self.speed

    # Set the angle of the img according to the shooting angle
    def update_img(self):
        self.image = pygame.transform.rotate(self.base_img, -(self.angle))
