'''
    Class representing objects on the map that cannot be passed.
    An obstacle can have hitpoints and be destroyed by the player. Some obstacles are indistructable.
    Obstacles might hurt the player, when she touches it.
'''
import pygame, funcs

class Obstacle(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, pos_x, pos_y, size, img_path): # Position on map and size in pixels(?)
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.image      = funcs.load_img(img_path)
        self.image      = pygame.transform.scale(self.image, (size[0],size[1]))
        self.rect       = self.image.get_rect()
        self.pos_x     = pos_x
        self.pos_y     = pos_y

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