# This file stores functions to generate some basic objects that will be part of most levels.

#-----------------------------------------------+
# Generate a tree object.
# - Random position
# - Randomly chosen image from all tree-images
# - Players cannot walk through trees
#-----------------------------------------------+
import random

from custom_classes import Weapon
from custom_classes import Item


#----------------------------------------------+
# Function to generate a tree on the level
#----------------------------------------------+
def tree_touched(player):
    player.bounce_back()

def generateTree(lvl, w, h):
    # Generate a name for the object ==> defines skin
    treeSkins   = {}
    for key, value in lvl.all_images.items():
        if 'tree' in str(key):
            treeSkins[key] = value
    type        = treeSkins.keys()[random.randint(0, len(treeSkins.keys())-1)]

    # Random position in the level
    x           = random.randint(0, len(lvl.texture_grid)-1)
    y           = random.randint(0, len(lvl.texture_grid[0])-1)

    # No rescaling of images
    # w           = treeSkins[type].get_rect().size[0]
    # h           = treeSkins[type].get_rect().size[1]

    thistree    = Item.Item(type, lvl, [x, y], [w, h], tree_touched, False)

    return thistree

#----------------------------------------------+
# Goal-Object: Reach the goal to win.
#----------------------------------------------+
def goal_touched(player):
    print "Player wins!"

def generateGoal(lvl, pos):
    thisGoal = Item.Item("teleporter", lvl, pos, [64, 64], goal_touched, False)
    return thisGoal

#----------------------------------------------+
# Function to create the basic weapon: Gun
#----------------------------------------------+
def generate_gun_dmg():
    dmg = random.randint(10, 30)
    return dmg

def generateGun():
    wpn = Weapon.Weapon("gun", 5, 0.3, generate_gun_dmg)
    return wpn

