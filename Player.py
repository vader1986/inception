#------------------------------------------------------------------------------+
# Player Class
#
# The player class contains all information about the player.
#
#------------------------------------------------------------------------------+
import pygame

import Constants


class Player(pygame.sprite.Sprite):

    name        = "Jeffrey"
    hitpoints   = [Constants.player_default_hitpts, Constants.player_default_hitpts] # A list with 2 items. Current_hitpoints and max_hittpoints
    position    = [] # Player's position in the level (x, y)
    speed       = Constants.player_default_speed # Players current speed
    inventory   = [] # Player's weapons
    equiped_weapon = 0 # Which weapon in the inventory is currently equiped
    medipacks   = Constants.player_default_medikits # Number of available medipacks

    def __init__(self, name, level):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.image      = level.all_images[Constants.player_img]
        player_img_size = self.image.get_size()  # Get player image size
        self.rect       = self.image.get_rect()
        self.rect.x     = pygame.display.Info().current_w / 2 - player_img_size[0] / 2
        self.rect.y     = pygame.display.Info().current_h / 2 - player_img_size[1] / 2