#------------------------------+
# Game class
#------------------------------+
import pygame
import Constants
from UI.MenuRenderer import MenuRenderer
from UI.LevelRenderer import LevelRenderer

from custom_classes import InputListener


class game(object):

    lvl     = None      # The currently played level. Is generated whenever player selects "start game" in main menu.
    screen  = None      # Screen to render the game on
    state   = "mainMenu"# Game state: mainMenu, ...
    keys    = {}        # A dictionary representing the key bindings

    #-----------------------------------------------+
    # Initialize a new game.
    #-----------------------------------------------+
    def __init__(self):

        self.load_settings()    # Load the current game settings
        pygame.init()           # Initialize pygame engine
        clock = pygame.time.Clock()         # Used to manage how fast the screen updates
        screen = pygame.display.set_mode((self.screen_w, self.screen_h))        # Set up the screen
        pygame.display.set_caption(Constants.game_title)

        # Start the game loop
        while True:
            # Start with a clear screen every time
            screen.fill(Constants.BLACK)
            # Recognise keyboard input
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            #TODO: Listen to inputs (make this class an inputlistener)
            # Render stuff depending on game state
            if self.state == "mainMenu":
                MenuRenderer.render()
            elif self.state == "playing":
                LevelRenderer.render()
            # 60 fps
            clock.tick(60)
            # Draw on screen
            pygame.display.flip()

    # -----------------------------------------------+
    # Load game paramters from local textfiles.
    # - Player name
    # - Key condfiguration, Screen resolution, ...
    # - (High-Scores?)
    # -----------------------------------------------+
    def load_settings(self):
        #TODO: check if settings.txt exists, if it does => load content
        self.playername  = "Jeff"
        self.keys        = {"up":Constants.up, "down":Constants.down, "left":Constants.left, "right":Constants.right,
                       "fire":Constants.fire, "next_w":Constants.next_w, "prev_w":Constants.prev_w}
        self.screen_w   = Constants.screen_width
        self.screen_h   = Constants.screen_height