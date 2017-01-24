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


class Player(pygame.sprite.Sprite):

    angle       = 0 # Viewing angle
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

    #------------------------------------+
    # Function to change the angle
    # and adjust the image accordingly
    # -----------------------------------+
    def turn(self, degree):
        self.angle+=degree
        orig_xy = self.rect.center
        # Rotate image
        self.image = pygame.transform.rotate(self.baseimage, -(self.angle))
        # Reposition
        self.rect.center = orig_xy

    # ------------------------------------+
    # Function to change the angle
    # and adjust the image accordingly
    # -----------------------------------+
    def move(self, direction):
        v = (math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180))
        new_pos_x = self.position[0] + v[0] * self.speed
        new_pos_y = self.position[1] + v[1] * self.speed
        if direction > 0:
            self.position[0] += v[0] * self.speed
            self.position[1] += v[1] * self.speed
        else:
            self.position[0] -= v[0] * self.speed
            self.position[1] -= v[1] * self.speed

    # ------------------------------------+
    # Return the currently used weapon
    # -----------------------------------+
    def get_current_weapon(self):
        return self.inventory[self.equiped_weapon]