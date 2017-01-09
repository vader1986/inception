# All helper functions

# Libraries
import os, pygame

# Load an image from the 'imgs' subfolder
def load_img(path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, path)
    this_img = pygame.image.load(abs_file_path).convert()
    return this_img

# Load a sound file
def load_sound(path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, path)
    this_sound = pygame.mixer.Sound(abs_file_path)
    return this_sound
