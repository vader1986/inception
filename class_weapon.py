'''
    Class weapon is relevant for all players.
    A player may carry multiple weapons but only
    one is active at a time. The active weapon
    defines the players img and generates projectiles
    when a player fires a shot.

    Each weapon has its own img to be displayed in the HUD.
'''
import pygame, class_projectile, random

class Weapon:
    # Constructor
    def __init__(self, name, mindam, maxdam, range, speed, rel_img_path_weapon, rel_img_path_char, rel_img_path_projectile):
        self.name                   = name
        self.mindam                 = mindam
        self.maxdam                 = maxdam
        self.range                  = range
        self.speed                  = speed
        self.rel_img_path_weapon    = rel_img_path_weapon
        self.rel_img_path_char      = rel_img_path_char
        self.rel_img_path_projectile= rel_img_path_projectile

    # Generate a new projectile (used when player fires a shot)
    def generateProjectile(self, x, y, angle):
        shot = class_projectile.Projectile(self.rel_img_path_projectile,
                                           x,
                                           y,
                                           angle,
                                           self.speed,
                                           random.randint(self.mindam, self.maxdam),
                                           self.range)
        return shot