#------------Main file of the game------------------------+
#
# Contains the game-loop and does all the rendering.
# Manages keyboard/joystick-inputs.
#
#---------------------------------------------------------+
import math
import random

from classes import Item
from classes import Level
from classes import Player
import pygame

import BasicObjects
import Constants
from classes import InputListener


#--------------------------------------------------------------------------------------------------------------+
# Functions
#--------------------------------------------------------------------------------------------------------------+

#--------------------------------------------------------------------------------------------------------------+
# Render player information on the screen (Hitpoints, Inventory, equiped weapon, weapon reload-time, medikits)
#--------------------------------------------------------------------------------------------------------------+
def renderHUD(screen, player):
    pass

#--------------------------------------------------------------------------------------------------------------+
# Render textures (just the ones that are needed to fill the screen
#--------------------------------------------------------------------------------------------------------------+
def renderTextures(level, screen_width, screen_height, screen):
    # Get the parts of the texture_grid that need to be rendered
    x_range     = math.ceil(screen_width/level.texture_size[0]/2.0)
    y_range     = math.ceil(screen_height/level.texture_size[1]/2.0)

    x_min       = max(0, int(level.player.position[0] - x_range)-1) # Indices cannot become negative
    x_max       = min(int(math.ceil(level.player.position[0] + x_range))+1, len(level.texture_grid))
    y_min       = max(0, int(level.player.position[1] - y_range)-1)
    y_max       = min(int(math.ceil(level.player.position[1] + y_range))+1, len(level.texture_grid[0])) # Maximum height is number of tiles of texture_grid

    for i in range(x_min, x_max): # Render each relevant texture
        for j in range(y_min, y_max):
            screen_pos_x = level.player.rect.centerx - (level.player.position[0] - i- 0.5)*level.texture_size[0]# Texture position on the screen relative to player
            screen_pos_y = level.player.rect.centery - (level.player.position[1] - j - 0.5)*level.texture_size[1]
            screen.blit(level.all_textures[level.all_textures.keys()[int(level.texture_grid[i,j]-1)]], (screen_pos_x, screen_pos_y))


# --------------------------------------------------------------------------------------------------------------+
# Render items that are visible on the screen
# --------------------------------------------------------------------------------------------------------------+
def renderItems(level, screen_width, screen_height, screen):

    # Get the parts of the texture_grid that need to be rendered
    x_range     = math.ceil(screen_width/level.texture_size[0]/2.0)
    y_range     = math.ceil(screen_height/level.texture_size[1]/2.0)

    x_min       = max(0, int(level.player.position[0] - x_range)-1) # Indices cannot become negative
    x_max       = min(int(math.ceil(level.player.position[0] + x_range))+1, len(level.texture_grid))
    y_min       = max(0, int(level.player.position[1] - y_range)-1)
    y_max       = min(int(math.ceil(level.player.position[1] + y_range))+1, len(level.texture_grid[0])) # Maximum height is number of tiles of texture_grid

    # Render all visible items
    for i in level.items:
        if x_min <= i.position[0] <= x_max and y_min <= i.position[1] <= y_max:
            level.render_items.add(i)
            screen_pos_x = level.player.rect.centerx - (level.player.position[0] - i.position[0] - 0.5) * level.texture_size[0]  # position on the screen relative to player
            screen_pos_y = level.player.rect.centery - (level.player.position[1] - i.position[1] - 0.5) * level.texture_size[1]
            i.rect.centerx = screen_pos_x
            i.rect.centery = screen_pos_y
        else:
            level.render_items.remove(i)
    level.render_items.draw(screen)


# --------------------------------------------------------------------------------------------------------------+
# Generate a random map - JUST FOR TESTING
#--------------------------------------------------------------------------------------------------------------+
def initRandomLevel(theme, width, height):
    lvl             = Level.Level(theme, width, height) # New empty level
    lvl.load_textures()                                 # Load textures
    #-------------------------+
    # Add player
    #-------------------------+
    player          = Player.Player("Imadummy", lvl)    # Add a dummy player
    player.position = [1, 1]
    lvl.player      = player
    #-------------------------+
    # Generate Texture grid
    #-------------------------+
    n_tex           = len(lvl.all_textures) # How many different textures are there
    for i in range(width-1):
        for j in range(height-1):
            lvl.texture_grid[i,j] = random.randint(0, n_tex-1)
    #-------------------------+
    # Add items
    #-------------------------+
    nitems          = width*height/50
    for i in range(0, nitems):
        lvl.items.add(BasicObjects.generateTree(lvl, 36, 48))
    return lvl

#--------------------------------------------------------------------------------------------------------------+
# Setup level, player, screen, etc.
#--------------------------------------------------------------------------------------------------------------+
pygame.init() # Initialize pygame engine

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Setup the screen
screen_w        = Constants.screen_width
screen_h        = Constants.screen_height
screen          = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption(Constants.game_title)

# Setup player and level
this_lvl = initRandomLevel("classic", 100,25)

# Setup the SpriteGroups
chars       = pygame.sprite.Group()

# Add elements to spriteGroups
chars.add(this_lvl.player)

#--------------------------------------------------------------------------------------------------------------+
#  Start the game
#--------------------------------------------------------------------------------------------------------------+
while True:
    ev          = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break

    # Move projectiles and villians
    this_lvl.update()

    # Input listener for keyboard (should be gamepad later as well)
    InputListener.listen(ev, this_lvl)

    # Collosion detection and handling
    touched = pygame.sprite.spritecollide(this_lvl.player, this_lvl.items, False)
    for i in touched:
        if type(i) is Item.Item:
            i.when_touched(this_lvl.player)

    # Rendering
    screen.fill(Constants.BLACK)  # Clear the screen
    renderTextures(this_lvl, screen_w, screen_h, screen)    # Render textures
    renderItems(this_lvl, screen_w, screen_h, screen)       # Render all items
    chars.draw(screen)  # Draw player

    # 60 fps
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
