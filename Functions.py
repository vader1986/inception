#------------------------------------------------+
# Collection of usefull functions
#------------------------------------------------+

import os
import pygame


# Load an image (assumes images are in a subfolder of the script itself
def load_img(path):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, path)
    this_img = pygame.image.load(abs_file_path).convert()
    return this_img
