#----------------------------------------+
# Class representing all items that
# are part of a level.
#----------------------------------------+
import pygame as pygame

import Functions


class Item(pygame.sprite.Sprite):

    name            = "tree"    # Name defines the image that will be loaded
    position        = []        # Position in level
    collusion_func  = None      # A function performing some action (with the player?) when touched by player
    only_once       = True
    first_touch     = True      # For some items it might be relevant if they were touched multiple times

    # Constructor
    def __init__(self, name, lvl, position, size, fun, only_once):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.name               = name
        self.position           = position
        scaled_image            = pygame.transform.scale(lvl.all_images[name], size)
        self.image              = scaled_image
        self.rect               = self.image.get_rect()
        self.collusion_func     = fun
        self.only_once          = only_once


    #------------------------------------------------------------+
    # Function that is triggered when a player touches the object
    # -----------------------------------------------------------+
    def when_touched(self, player):
        if self.first_touch and self.only_once:
            self.collusion_func(player)
            self.first_touch = False
        elif not self.only_once:
            self.collusion_func(player)