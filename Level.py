#------------------------------------------------------------------------------+
# Level Class
#
# The level is the central class of the game. It contains information
# about the level itself and everything that is in the level.
#
#------------------------------------------------------------------------------+
import os

import numpy

import Functions


class Level():

    theme           = "classic"
    all_textures    = {} # A dictionary storing all texture that will be used in the level (which depends on theme)
    all_images      = {} # A dictionary of all images used for objects, items, etc.
    texture_size    = [] # The dimension of textures in pixels (widht, height)
    texture_grid    = [] # An 2-dimensional array defining which ground textures are used where in the level
    items           = [] # An array containing all objects that are part of the level (obstacles, villians, items, projectiles)
    player          = [] # An object of class player

    def __init__(self, theme, width, height):
        self.theme          = theme                         # Set the theme
        self.texture_grid   = numpy.zeros((width, height))  # Set level dimension


    # Load all relevant textures/images for the level - based on its' theme
    def load_textures(self):
        # get a list of all files in according directory
        txtr_files  = os.listdir("imgs/" + self.theme + "/")
        for i in txtr_files:
            this_name               = i[3:(len(i)-4)] # Remove the leading indicator if image is texture or not and remove the image file ending
            if "bg_" in i:
                self.all_textures[this_name]    = Functions.load_img("imgs/" + self.theme + "/" + i)
            else:
                self.all_images[this_name]      = Functions.load_img("imgs/" + self.theme + "/" + i)
        # Update the texture size
        self.texture_size       = self.all_textures[self.all_textures.keys()[0]].get_rect().size