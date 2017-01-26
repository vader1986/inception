#------------------------------------------------------------------------------+
# Player Class
#
# The player class contains all information about the player.
#
#------------------------------------------------------------------------------+
import pygame
import math

import BasicObjects
import Constants
import custom_classes.Character

class Player(custom_classes.Character.Character):

    angle       = 0  # Viewing angle
    moving_dir  = 1  # postive number represent moving to the front, negative number show we last moved back
    position    = [] # Player's position in the level (x, y)
    speed       = Constants.player_default_speed # Players current speed
    baseimage   = None # The base image, is needed to generate the roated and scaled versions
    name        = "Jeffrey"
    hitpoints   = [Constants.player_default_hitpts, Constants.player_default_hitpts] # A list with 2 items. Current_hitpoints and max_hittpoints
    inventory   = [] # Player's weapons
    equiped_weapon = 0 # Which weapon in the inventory is currently equiped
    medipacks   = Constants.player_default_medikits # Number of available medipacks


    def __init__(self, name, level):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.baseimage  = level.all_images[Constants.player_img]
        self.image      = self.baseimage
        self.rect       = self.image.get_rect()
        self.rect.centerx = pygame.display.Info().current_w/2
        self.rect.centery = pygame.display.Info().current_h / 2
        # By default add a gun to the inventory
        self.inventory.append(BasicObjects.generateGun())

    # ------------------------------------+
    # Function to move the player
    # -----------------------------------+
    def move(self, direction, lvl):
        v = (math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180))
        if direction > 0:
            new_x = self.position[0] + v[0] * self.speed
            new_y = self.position[1] + v[1] * self.speed
        else:
            new_x = self.position[0] - v[0] * self.speed
            new_y = self.position[1] - v[1] * self.speed
        if 0 <= new_x <= len(lvl.texture_grid) and 0 <= new_y <= len(lvl.texture_grid[0]): # Cannot go outside the level
            self.position = [new_x, new_y]
        self.moving_dir = direction

    # ------------------------------------+
    # Bounce back method moves player to the
    # previous position. Used by non-passable
    # objects.
    # ------------------------------------+
    def bounce_back(self):
        v = (math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180))
        new_x = self.position[0] + v[0] * self.speed * self.moving_dir*(-1) # Move just opposite to what we did before
        new_y = self.position[1] + v[1] * self.speed * self.moving_dir*(-1)
        self.position = [new_x, new_y]

    # ------------------------------------+
    # Return the currently used weapon
    # -----------------------------------+
    def get_current_weapon(self):
        return self.inventory[self.equiped_weapon]