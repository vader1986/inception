'''
Contains all important classes for the game.
'''

# Libraries
import sys, pygame, os

#----------------+
# Player Class
#----------------+
class Player():
    """Class for the player object."""
# player attributes
    name = "Jeffrey"    # player Name
    position = {"x":0,
                "y":0}  # player's position on map
    angle = 0           # player's viewing direction
    hitpts = 100        # player's life points
    alive = True        # is player alive
    inventory = []      # player's inventory (weapons, medicits, ...)

# constructor
    def __init__(self, name, hitpts, inventory):
        self.name = name
        self.hitpts = hitpts
        self.inventory = inventory

# print method
    def print_player(self):
        print "Player:          " + self.name
        print "Hitpoints:       " + self.hitpts
        print "Position (x/y):  (" + str(self.position["x"]) + "/" + str(self.position["y"]) + ")"

# move player
    def move(self, xchange, ychange):
        self.x+=xchange
        self.y+=ychange

# when player gets hit
    def hurtme(self, dmg):
        self.hitpts-=dmg
        if self.hitpts<=0:
            self.alive = False
            print self.name + " died! Nooooooo"



# Start GAME and stuff

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