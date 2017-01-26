#------------------------------------------------------------------------------+
# Level Class
#
# The level is the central class of the game. It contains information
# about the level itself and everything that is in the level.
#
#------------------------------------------------------------------------------+
import os

import numpy
import pygame

import Functions
from custom_classes import Projectile


class Level():

    theme           = "classic"
    all_textures    = {}        # A dictionary storing all texture that will be used in the level (which depends on theme)
    all_images      = {}        # A dictionary of all images used for objects, items, etc.
    texture_size    = []        # The dimension of textures in pixels (widht, height)
    texture_grid    = []        # An 2-dimensional array defining which ground textures are used where in the level
    items           = pygame.sprite.Group() # A spriteGroup containing all items in the level
    render_items    = pygame.sprite.Group() # A spriteGroup that contains only the items that should be rendered
    player          = []                    # The sprite representing the player
    chars           = pygame.sprite.Group() # All characters on the map. The first character in the group is always the player
    render_chars    = pygame.sprite.Group() # All the villians that are currently visible
    projectiles     = pygame.sprite.Group()
    render_projectiles = pygame.sprite.Group() # A separate group managing the projectiles

    #-----------------------------------------------------------------------+
    # Constructor
    #-----------------------------------------------------------------------+
    def __init__(self, theme, width, height):
        self.theme          = theme                         # Set the theme
        self.texture_grid   = numpy.zeros((width, height))  # Set level dimension

    #-----------------------------------------------------------------------+
    # Load all relevant textures/images for the level - based on its' theme
    #-----------------------------------------------------------------------+
    def load_textures(self):
        # get a list of all files in according directory
        txtr_files  = os.listdir("imgs/" + self.theme + "/")
        for i in txtr_files:
            if i[0] != ".":
                this_name               = i[3:(len(i)-4)] # Remove the leading indicator if image is texture or not and remove the image file ending
                if "bg_" in i:
                    self.all_textures[this_name]    = Functions.load_img("imgs/" + self.theme + "/" + i)
                else:
                    self.all_images[this_name]      = Functions.load_img("imgs/" + self.theme + "/" + i)
        # Update the texture size
        self.texture_size       = self.all_textures[self.all_textures.keys()[0]].get_rect().size

    #-----------------------------------------------------------------------+
    # Generate a projectile whenever a character fires a shot
    #-----------------------------------------------------------------------+
    def char_fire(self, char):
       # Generate a projectile
        proj            = Projectile.Projectile(self, char)
        self.projectiles.add(proj)
        return proj

    #-----------------------------------------------------------------------+
    # Function to be called by the game loop.
    # Will move projectiles and villians
    #-----------------------------------------------------------------------+
    def update(self):
        for i in self.projectiles:
            i.move_me()

