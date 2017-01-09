# All helper functions

# Libraries
import os, pygame, class_player

# Params
RED = (255,0,0)

# Load an image from the 'imgs' subfolder
def load_img(path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, path)
    this_img = pygame.image.load(abs_file_path).convert()
    return this_img

# Load a sound file
def load_sound(path):
    if pygame.mixer.get_init() == None:
        pygame.mixer.init(44100, -16, 2, 2048)
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, path)
    this_sound = pygame.mixer.Sound(abs_file_path)
    return this_sound

# Draw the HUD
def draw_HUD(player, screen):
    # Get information about the screen (dimension)
    screen_info     = pygame.display.Info()

    # Draw a rectangle containing an img representing the currently used weapon
    height          = 50
    width           = 50
    img             = load_img("imgs/" + player.theme + "/weapon/" + player.inventory[player.equiped_weapon].name + ".gif")
    img             = pygame.transform.scale(img, (width, height))
    img_rect        = img.get_rect()
    x               = screen_info.current_w / 2 - width / 2
    y               = screen_info.current_h - height - 5
    img_rect.x      = x
    img_rect.y      = y
    # Draw the stuff
    pygame.draw.rect(screen, RED, (x, y, width, height), 0)
    screen.blit(img, img_rect)
