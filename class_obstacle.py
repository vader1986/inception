'''
    Class representing objects on the map that cannot be passed.
    An obstacle can have hitpoints and be destroyed by the player. Some obstacles are indistructable.
    Obstacles might hurt the player, when she touches it.
'''
import pygame

class Obstacle(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, pos_x, pos_y, size): # Position on map and size in pixels(?)
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites

    # Do something when player touches the obstacle
    def is_touched(self):
        # Play sound?
        # Play animation?
        pass # Return dmg

    # What happens when the obstacle is hit by a projectile
    def get_hit(self, dmg):
        pass

    def set_hitpoints(self, maxhit):
        # If maxhit = -1 => indistructable (?)
        pass

    def set_img(self, rel_img_path):
        # load theme-specific img
        pass