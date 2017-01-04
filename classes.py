'''
Contains all important classes for the game.
'''

# Libraries
import sys, pygame, os

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
        print "Hitpoints:       " + self.hitpts
        print "Position (x/y):  (" + str(self.position["x"]) + "/" + str(self.position["y"]) + ")"

# when player gets hit
    def hurtme(self, dmg):
        self.hitpts-=dmg
        if self.hitpts<=0:
            self.alive = False
            print self.name + " died! Nooooooo"



# Start GAME and stuff
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

# Create a RED player block
player = Player("Basti", 1000, [])
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
speed = [0, 0]
while not done:


    player.rect.x += speed[0]
    player.rect.y += speed[1]

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

'''
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "imgs/hero.png"
abs_file_path = os.path.join(script_dir, rel_path)
hero = pygame.image.load(abs_file_path)
ballrect = hero.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-2, 0]
            if event.key == pygame.K_RIGHT:
                speed = [2, 0]
            if event.key == pygame.K_UP:
                speed = [0, -2]
            if event.key == pygame.K_DOWN:
                speed = [0, 2]
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        ballrect = ballrect.move(speed)
        speed = [0, 0]

    screen.fill(black)
    screen.blit(hero, ballrect)
    pygame.display.flip()
'''