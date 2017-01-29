#--------------------------------------------------+
# Class representing a menu item in the main menu
#--------------------------------------------------+
import pygame


class Menu_item(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, text):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.text           = text