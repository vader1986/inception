#------------------------------------+
# File containing game parameters
#------------------------------------+

# Game parameters
import pygame

game_title      = "Inception"
screen_width    = 400
screen_height   = 320

# Fonts
pygame.font.init()
menuFont        = pygame.font.Font("fonts/kenvector_future.ttf", 20)

# Colors
BLACK           = (0,0,0)
WHITE           = (255, 255, 255)
RED             = (255,0,0)

# Player default attributs
player_default_speed        = 0.15
player_default_hitpts       = 100
player_default_medikits     = 3
player_default_turn_speed   = 5

# Image names, used for objects/textures etc.
player_img      = "player"
tree_img        = "tree"

# Default key bindings
up      = pygame.K_UP
down    = pygame.K_DOWN
left    = pygame.K_LEFT
right   = pygame.K_RIGHT
fire    = pygame.K_SPACE
next_w  = pygame.K_e
prev_w  = pygame.K_q