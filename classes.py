'''
Contains all important classes for the game.
'''

# Libraries
import sys, pygame, os, random

#----------------+
# Player Class
#----------------+
class Player(pygame.sprite.Sprite):
    """Class for the player object."""
# player attributes
    name = "Jeffrey"    # player Name
    angle = 0           # player's viewing direction
    hitpts = 100        # player's life points
    alive = True        # is player alive
    inventory = []      # player's inventory (weapons, medicits, ...)

# constructor
    def __init__(self, name, hitpts, inventory):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.hitpts = hitpts
        self.inventory = inventory
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "imgs/hero.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.image = pygame.image.load(abs_file_path).convert()
        self.rect = self.image.get_rect()

    # print method
    def print_player(self):
        print "Player:          " + self.name
        print "Hitpoints:       " + str(self.hitpts)

# when player gets hit
    def hurtme(self, dmg):
        if self.alive:
            self.hitpts-=dmg
            if self.hitpts<=0:
                self.alive = False
                print self.name + " died! Nooooooo"

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
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()


for i in range(10):
    obs = Obstacle(screen_width, screen_height)
    block_list.add(obs)
    all_sprites_list.add(obs)

# Create the player
player = Player("Basti", 100, [])
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
speed = [0, 0]
while not done:
    # Move the player
    player.rect.x += speed[0]
    player.rect.y += speed[1]
    # Check for collusions
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    if len(blocks_hit_list) > 0:
        player.hurtme(1)
        player.print_player()
    # control movement direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-5, 0]
            if event.key == pygame.K_RIGHT:
                speed = [5, 0]
            if event.key == pygame.K_UP:
                speed = [0, -5]
            if event.key == pygame.K_DOWN:
                speed = [0, 5]
        if event.type == pygame.KEYUP:
            speed = [0, 0]

    # Clear the screen
    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()