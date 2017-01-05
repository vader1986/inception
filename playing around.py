'''
Contains all important classes for the game.
'''

# Libraries
import sys, pygame, os, random, math, class_character


# Helper functions

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
    '''obstacles!'''

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


#-----------------------------------------------+
# Start GAME and stuff
#-----------------------------------------------+


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()


for i in range(10):
    obs = Obstacle(screen_width, screen_height)
    block_list.add(obs)
    all_sprites_list.add(obs)

# Create the player
player = Player("Basti", [])
player.rect.x = 150
player.rect.y = 150

all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
font = pygame.font.SysFont("menlo", bold=True, size=12)

while not done:
    # Check for collusions
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    if len(blocks_hit_list) > 0:
        print "Bumms"

    # control movement direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.turn_left(5)
            if event.key == pygame.K_RIGHT:
                player.turn_right(5)
            if event.key == pygame.K_UP:
                player.speed = abs(player.speed)
                player.move_me()
            if event.key == pygame.K_DOWN:
                player.speed = -abs(player.speed)
                player.move_me()
        print player.angle
        player.adjust_img()

    # Clear the screen
    screen.fill(WHITE)

    all_sprites_list.draw(screen)

    # HUD: Print stats
    screen.blit(font.render("Player: " + player.name, 1, RED), (10, 5))
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()