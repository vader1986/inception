# Super class for all characters in the game

# Libraries
import math
import pygame
import funcs
import class_projectile


# Character class
class Character(pygame.sprite.Sprite):

    inventory       = [] # A List containing all available weapons
    equiped_weapon  = -1 # Id number which weapon is active
    angle           = 0

    # Constructor
    def __init__(self, maxhitpoints, hitpoints, speed, rel_path_img):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.maxhitpoints   = maxhitpoints
        self.hitpoints      = hitpoints
        self.speed          = speed
        self.image          = funcs.load_img(rel_path_img)
        self.base_img       = self.image
        self.rect           = self.image.get_rect()

    # Move the character in the direction she is looking (self.angle)
    def move(self):
        v = [math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180)]
        self.rect.x += v[0] * self.speed
        self.rect.y += v[1] * self.speed

    # Rotate the character to the left or right side
    def turn(self, increment, direction):
        # Set the character's angle into the right direction
        if direction == "right":
            if self.angle+increment<360:
             self.angle+=increment
            else:
             self.angle=self.angle+increment-360
        else:
            if self.angle - increment > 0:
                self.angle -= increment
            else:
                self.angle = self.angle - increment + 360
        # Rotate the characters image into the right direction
        self.update_img()

    # Update the image, when character rotates
    def update_img(self):
        self.image = pygame.transform.rotate(
                self.base_img, -(self.angle))

    # Shoot
    def fire(self):
        if self.equiped_weapon == - 1:
            print "I don't have a weapon! :-("
            return None
        else:
            v       = [math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180)]
            shot    = self.inventory[self.equiped_weapon].generateProjectile(   self.rect.x + v[0],
                                                                                self.rect.y + v[1],
                                                                                self.angle)
            return shot

    # Add a weapon to the inventory and make it the currently used weapon
    def add_weapon(self, weapon):
        self.inventory.append(weapon)
        self.equiped_weapon = len(self.inventory)-1
        print "Using " + weapon.name + " now."

    # Change the used weapon (direction is 1 for next weapon, -1 for previous weapon)
    def next_weapon(self, direction):
        if direction == 1: # Next weapon
            if self.equiped_weapon+1 > len(self.inventory)-1: # If you are already using the last weapon in inv go to first
                self.equiped_weapon = 0
            else: # Next weapon
                self.equiped_weapon+=1
        else:
            if self.equiped_weapon-1 < 0: # If you are already using the first weapon => take last
                self.equiped_weapon = len(self.inventory)-1
            else: # Previous weapon
                self.equiped_weapon-=1
        print "Using " + self.inventory[self.equiped_weapon].name + " now."


    # When character is hit by a projectile
    def get_hit(self, dmg):
        self.hitpoints-=dmg
        if self.hitpoints <=0:
            self.rect.x = -100
            self.rect.y = -100
            pygame.sprite.Sprite.kill(self)
            print "Buhuuuu"