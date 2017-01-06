'''
Contains all important classes for the game.
'''

# Libraries
import sys, pygame, os, random, math, class_character

#-----------------------------------------------+
# Start GAME and stuff
#-----------------------------------------------+
# Settings
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# Initialize Pygame
pygame.init()

# fonts = pygame.font.get_fonts()
# for i in fonts:
#    print i
font = pygame.font.SysFont("arial", bold=True, size=12)

# Set the height and width of the screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode([screen_width, screen_height])

# List with all character sprites
chars = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Create the player
player = class_character.Character(100, 95, 5, "imgs/Hero.png")
player.rect.x = 150
player.rect.y = 150

chars.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Use Joystick
pygame.joystick.init()
js = pygame.joystick.Joystick(0)
js.init()

# -------- Main Program Loop -----------
turnleft    = False
turnright   = False
move   = False

while not done:
    # control movement direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # JOYSTICK
        if event.type == pygame.JOYHATMOTION:
            evt = js.get_hat(0)
            if evt[0] == -1: # left
                turnleft = True
            if evt[0] == 1:
                turnright = True
            if evt[1] == 1:
                move = True
                player.speed = abs(player.speed)
            if evt[1] == -1:
                move = True
                player.speed = -abs(player.speed)
            if evt[0] == 0:
                turnright   = False
                turnleft    = False
            if evt[1] == 0:
                move = False
        if event.type == pygame.JOYBUTTONDOWN:
            evt = js.get_button(1)
            if evt == 1:
                shot = player.fire()
                shots.add(shot)
        # KEYBOARD
        # React to pressed keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turnleft = True
            if event.key == pygame.K_RIGHT:
                turnright = True
            if event.key == pygame.K_UP:
                move = True
                player.speed = abs(player.speed)
            if event.key == pygame.K_DOWN:
                move = True
                player.speed = -abs(player.speed)
            if event.key == pygame.K_SPACE:
                shot = player.fire()
                shots.add(shot)

        # React to key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                turnleft = False
            if event.key == pygame.K_RIGHT:
                turnright = False
            if event.key == pygame.K_UP:
                move = False
            if event.key == pygame.K_DOWN:
                move = False
    if move:
        player.move()
    if turnright:
        player.turn(5, "right")
    if turnleft:
        player.turn(5, "left")

    # Clear the screen
    screen.fill(WHITE)

    chars.draw(screen)

    for i in shots:
        i.move()

    shots.draw(screen)

    # HUD: Print stats
    screen.blit(font.render("Hitpoints: " + str(player.hitpoints) + "/" + str(player.maxhitpoints), 1, RED), (10, 5))

    # 60 fps
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()



'''
# Loads an image from a given relative path
def load_img(path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, path)
    this_img = pygame.image.load(abs_file_path).convert()
    return this_img

#----------------+
# Player Class
#----------------+
class Player(class_character.Character):
    """Class for the player object."""
# player attributes
    name = "Jeffrey"    # player Name
    inventory = []      # player's inventory (weapons, medicits, ...)
    base_img = []
# constructor
    def __init__(self, name, inventory):
        pygame.sprite.Sprite.__init__(self)  # needed
        self.name = name
        self.inventory = inventory
        self.image = load_img("imgs/Hero.png")
        self.base_img = self.image
        self.rect = self.image.get_rect()

    # Set Image angle
    def adjust_img(self):
        self.image = pygame.transform.rotate(
                self.base_img, -(self.angle))

#----------------------+
# obstackle class
#----------------------+
class Obstacle(pygame.sprite.Sprite):

# Constructor
    def __init__(self, maxx, maxy):
        pygame.sprite.Sprite.__init__(self)
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "imgs/stone.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.image = pygame.image.load(abs_file_path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, maxx)
        self.rect.y = random.randint(0, maxy)

for i in range(10):
    obs = Obstacle(screen_width, screen_height)
    block_list.add(obs)
    all_sprites_list.add(obs)

# Check for collusions
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    if len(blocks_hit_list) > 0:
        print "Bumms"


'''