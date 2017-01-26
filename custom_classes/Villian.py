#------------------------------------------------------------------------------+
# Villian Class
#
# Villians are characters very similar like players. The main difference is
# that they are controlled by the game.
#
#------------------------------------------------------------------------------+
import pygame, custom_classes

import BasicObjects


class Villian(custom_classes.Character.Character):

    name            = "zombie"  # Determines used image and behaviour(?)
    hitpts          = [100,100] # Current and Maximum hitpoints
    angle           = 0         # Angle of view
    viewing_range   = 10        # When does the villian react to the player? texture grid dimension
    position        = []        # Level position
    inventory       = []        # Available weapons
    equiped_weapon  = 0         # Currently used weapon

    # Constructor
    def __init__(self, name, level, position):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.baseimage  = level.all_images[ name ] # Load the right image
        self.image      = self.baseimage
        self.rect       = self.image.get_rect()
        self.position   = position
        # By default add a gun to the inventory
        self.inventory.append(BasicObjects.generateGun())
