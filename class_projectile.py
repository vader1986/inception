# Projectiles are fired by characters

import pygame, funcs, math

class Projectile(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, rel_path_img, x, y, angle, speed, dmg, maxdist):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.image      = funcs.load_img(rel_path_img)
        self.base_img   = self.image
        self.rect       = self.image.get_rect()
        self.dmg        = dmg
        self.rect.x     = x
        self.rect.y     = y
        self.origin     = [x, y]
        self.angle      = angle
        self.speed      = speed
        self.maxdist    = maxdist
        self.update_img()

    # Move the projectile
    def move(self):
        v       = [math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180)] # Direction we are moving
        newpos  = [self.rect.x + v[0] * self.speed, self.rect.y + v[1] * self.speed] # New Position
        dist    = math.sqrt((self.origin[0]-newpos[0])**2 + (self.origin[1] - newpos[1])**2) # Distance from original position
        if dist >= self.maxdist: # If the projectile has reached maximum distance kill it
            self.kill()
        else: # Move the projectile
            self.rect.x = newpos[0]
            self.rect.y = newpos[1]

    # Set the angle of the img according to the shooting angle
    def update_img(self):
        self.image = pygame.transform.rotate(self.base_img, -(self.angle))
