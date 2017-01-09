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
    def __init__(self, name, mindam, maxdam, range, speed):
        self.name                   = name
        self.mindam                 = mindam
        self.maxdam                 = maxdam
        self.range                  = range
        self.speed                  = speed

    # Generate a new projectile (used when player fires a shot)
    def generateProjectile(self, theme, x, y, angle):
        shot = class_projectile.Projectile("imgs/" + theme + "/weapon/" + self.name + "_projectile.gif",
                                           x,
                                           y,
                                           angle,
                                           self.speed,
                                           random.randint(self.mindam, self.maxdam),
                                           self.range)
        return shot