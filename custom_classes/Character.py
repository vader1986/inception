#------------------------------------------------------------------------------+
# Character Class
#
# Parent class for Players and Villians.
#------------------------------------------------------------------------------+
import pygame

class Character(pygame.sprite.Sprite):

    name            = ""            # Determines img for villians
    angle           = 0             # Angle of view
    position        = []            # Character's position in the level (x, y)
    speed           = None          # Current speed
    baseimage       = None          # The base image, is needed to generate the roated and scaled versions
    inventory       = []            # List of available weapons
    equiped_weapon  = 0             # Which weapon in the inventory is currently equiped

    #------------------------------------+
    # Function to change the angle
    # and adjust the image accordingly
    # -----------------------------------+
    def turn(self, degree):
        self.angle+=degree          # Update angle of view
        orig_xy = self.rect.center  # Save the original position on screen// pygame moves the image when rotating
        self.image = pygame.transform.rotate(self.baseimage, -(self.angle)) # Rotate
        self.rect.center = orig_xy  # Center around the original position

    #-------------------------------------+
    # Damage handling function
    # ------------------------------------+
    def get_hit(self, projectile):
        self.hitpoints[0]-=projectile.dmg
        projectile.kill()
        if self.hitpoints[0] <= 0:
            self.kill()
