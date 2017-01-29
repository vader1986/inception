#------------Main file of the game------------------------+
#
# Contains the game-loop and does all the rendering.
# Manages keyboard/joystick-inputs.
#
#---------------------------------------------------------+
import math
import random

import pygame

import BasicObjects
import Constants
import Functions
from custom_classes import InputListener
from custom_classes import Item
from custom_classes import Level
from custom_classes import Main_Menu
from custom_classes import Menu_Item
from custom_classes import Player

#--------------------------------------------------------------------------------------------------------------+
# Game Parameters
#--------------------------------------------------------------------------------------------------------------+
game_state = "main_menu"    # Available game states: main_menu, configure, set_name, play_level, end_level

#--------------------------------------------------------------------------------------------------------------+
# Functions
#--------------------------------------------------------------------------------------------------------------+

#--------------------------------------------------------------------------------------------------------------+
# Render player information on the screen (Hitpoints, Inventory, equiped weapon, weapon reload-time, medikits)
#--------------------------------------------------------------------------------------------------------------+
from custom_classes import Villian


def renderHUD(screen, player):
    pass

#--------------------------------------------------------------------------------------------------------------+
# Render textures (just the ones that are needed to fill the screen
#--------------------------------------------------------------------------------------------------------------+
# Get the texture-grid min-and-max indicies for the things to be rendered
def get_render_rect(level, screen_width, screen_height):
    # Get the parts of the texture_grid that need to be rendered
    x_range     = math.ceil(screen_width/level.texture_size[0]/2.0)
    y_range     = math.ceil(screen_height/level.texture_size[1]/2.0)

    x_min       = max(0, int(level.player.position[0] - x_range)-1) # Indices cannot become negative
    x_max       = min(int(math.ceil(level.player.position[0] + x_range))+1, len(level.texture_grid))
    y_min       = max(0, int(level.player.position[1] - y_range)-1)
    y_max       = min(int(math.ceil(level.player.position[1] + y_range))+1, len(level.texture_grid[0])) # Maximum height is number of tiles of texture_grid
    return [x_min, x_max, y_min, y_max]

# Collect all textures that should be rendered and then draw them
def renderTextures(level, screen_width, screen_height, screen):

    render_rect = get_render_rect(level, screen_width, screen_height)

    for i in range(render_rect[0], render_rect[1]): # Render each relevant texture
        for j in range(render_rect[2], render_rect[3]):
            screen_pos_x = level.player.rect.centerx - (level.player.position[0] - i + .5)*level.texture_size[0]# Texture position on the screen relative to player
            screen_pos_y = level.player.rect.centery - (level.player.position[1] - j + .5)*level.texture_size[1]
            screen.blit(level.all_textures[level.all_textures.keys()[int(level.texture_grid[i,j]-1)]], (screen_pos_x, screen_pos_y))


# --------------------------------------------------------------------------------------------------------------+
# Render items/villians that are visible on the screen
# --------------------------------------------------------------------------------------------------------------+
# Set the image position of a Sprite to the correct position on the screen
def set_screen_pos(level, item):
    screen_pos_x = level.player.rect.centerx - (level.player.position[0] - item.position[0] - 0.5) * level.texture_size[0]
    screen_pos_y = level.player.rect.centery - (level.player.position[1] - item.position[1] - 0.5) * level.texture_size[1]
    item.rect.centerx = screen_pos_x
    item.rect.centery = screen_pos_y

def renderItems(level, screen_width, screen_height, screen):

    render_rect = get_render_rect(level, screen_width, screen_height)

    # Render all visible items
    for i in level.items:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            level.render_items.add(i)
            set_screen_pos(level, i)
        else:
            level.render_items.remove(i)

    # Add projectiles to list of things to render
    for i in level.projectiles:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            level.render_projectiles.add(i)
            set_screen_pos(level, i)
        else:
            level.render_projectiles.remove(i)

    # Add villians to list of things to render
    for i in level.chars:
        if render_rect[0] <= i.position[0] <= render_rect[1] and render_rect[2] <= i.position[1] <= render_rect[3]:
            level.render_chars.add(i)
            set_screen_pos(level, i)
        else:
            level.render_chars.remove(i)

    # Now draw the stuff
    level.render_chars.draw(screen)
    level.render_items.draw(screen)
    level.render_projectiles.draw(screen)


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
    player.position = [10, 10]
    lvl.player      = player
    lvl.render_chars.add(player)
    #-------------------------+
    # Add some zombies
    #-------------------------+
    for i in range(0, 10):
        lvl.chars.add(Villian.Villian("zombie", lvl, [random.randint(1, width), random.randint(1, height-1)]))
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

#    lvl.items.add(BasicObjects.generateGoal(lvl, [10, 10]))
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
this_lvl = initRandomLevel("classic", 100, 25)


#----------------------------------------------+
# Setup the Main Menu
#----------------------------------------------+
menuItems  = [Menu_Item.Menu_item("START GAME"), Menu_Item.Menu_item("CHANGE NAME"), Menu_Item.Menu_item("CONTROLS")]
mainMenu   = Main_Menu.Main_Menu(menuItems, Functions.load_img("menu_imgs/active_button.png"), Functions.load_img("menu_imgs/passive_button.png"))

#--------------------------------------------------------------------------------------------------------------+
#  Start the game
#--------------------------------------------------------------------------------------------------------------+
while True:
    ev          = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break

    #-----------------------------------+
    # Playing the level
    #-----------------------------------+
    if game_state == "main_menu":
        screen.fill(Constants.BLACK)  # Clear the screen
        mainMenu.render_menu(screen, screen_w, screen_h, 30)
        InputListener.listen(ev, mainMenu, this_lvl, game_state)
    #-----------------------------------+
    # Playing the level
    #-----------------------------------+
    elif game_state == "play_level":
        # Move projectiles and villians
        this_lvl.update()

        # Input listener for keyboard (should be gamepad later as well)
        InputListener.listen(ev, mainMenu, this_lvl)

        # Collosion detection and handling
        touched = pygame.sprite.spritecollide(this_lvl.player, this_lvl.items, False)
        for i in touched:
            if type(i) is Item.Item:
                i.when_touched(this_lvl.player)

        # Check if projectiles hit villians
        char_got_hit = pygame.sprite.groupcollide(this_lvl.chars, this_lvl.render_projectiles, False, False)
        for i in char_got_hit:
            i.get_hit(char_got_hit[i][0])

        # Rendering
        screen.fill(Constants.BLACK)  # Clear the screen
        renderTextures(this_lvl, screen_w, screen_h, screen)    # Render textures
        renderItems(this_lvl, screen_w, screen_h, screen)       # Render all items

    # 60 fps
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
