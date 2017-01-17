'''
    The game's level class.

    A level contains information about:
    - The graphics/sound theme that is used
    - Dimension of the map
    - A texture grid: Contain information about which texture to use where
    - Location of Start and Goal
    - Location ob obstacles

'''
import class_character, class_player, class_obstacle, math, pygame, funcs, random, os

class Level:

    obstacles       = [] # A list of obstacles
    characters      = [] # A list of villians
    texture_grid    = [] # A two dimensional array of integers. Each integer represents one texture on the map.
    theme           = "classic"
    textures        = [] # storing all textures as images) for given theme

    def __init__(self):
        pass

    # Add an obstacle to the level
    def add_obstacle(self, obs):
        self.obstacles.append(obs)

    # Add an character to the level
    def add_char(self, char):
        self.characters.append(char)

    # Get a list with all elements in viewing range of the player
    def get_elements(self, player, maxdist):
        res = [] # Collect all chars, items and obstacles in the given region
        for i in self.characters:
            if math.hypot(player.rect.x - i.rect.x, player.rect.y - i.rect.y) <= maxdist:
                res.append(i)
        for i in self.obstacles:
            if math.hypot(player.rect.x - i.rect.x, player.rect.y - i.rect.y) <= maxdist:
                res.append(i)
        return res

    # Store the sreen information in object to not need to get it every time
    def set_screen(self, screen):
        screen_info     = pygame.display.Info()
        self.screen_w   = screen_info.current_w
        self.screen_h   = screen_info.current_h

    # Function to draw what is currently on the screen
    def draw_view(self, player, screen):
        # TODO: Check if self.screen_w and self.screen_h are set
        # what is the screen-part of the level?
        xmin = player.level_pos_x - self.screen_w/2
        xmax = player.level_pos_x + self.screen_w/2
        ymin = player.level_pos_y - self.screen_h/2
        ymax = player.level_pos_y + self.screen_h/2
        # Check which items should be on the screen
        for i in self.obstacles: # Add items that are in the screen range ==> will be printed
            if xmin < i.pos_x < xmax and ymin < i.pos_y < ymax:
                # Now set the obstacles.rect.x and y correctly relative to the player, who is in the center of the screen
                i.rect.x    = player.rect.x + (i.pos_x - player.level_pos_x)
                i.rect.y    = player.rect.y + (i.pos_y - player.level_pos_y)
                screen.blit(i.image, i.rect)
        #TODO: Do the same for characters and items

    # Generate a random texture_grid
    # - width and height are the number of textures in both directions
    #   the map size is defined by the number of textures * texture_size
    def generate_random_texture_grid(self, width, height):
        self.load_textures()
        tex = [] # Store the integers
        for i in range(width):
            tex.append([])
            for j in range(height):
                tex[i].append(random.randint(1, len(self.textures)))
        self.texture_grid = tex

    # load all textures for a given theme
    def load_textures(self):
        # get a list of all files in according directory
        txtrs   = os.listdir("imgs/" + self.theme + "/textures/")
        imgs    = []
        for i in txtrs:
            imgs.append(funcs.load_img("imgs/" + self.theme + "/textures/" + i))
        self.textures = imgs

    # Draw the required textures on the screen
    def draw_textures(self, player, screen):
        # TODO: Check if self.screen_w and self.screen_h are set
        # what is the screen-part of the level?
        xmin = player.level_pos_x - self.screen_w/2
        xmax = player.level_pos_x + self.screen_w/2
        ymin = player.level_pos_y - self.screen_h/2
        ymax = player.level_pos_y + self.screen_h/2

        texture_dim = self.textures[0].get_rect().size[0]

        for i in range(len(self.texture_grid)):
            for j in range(len(self.texture_grid[i])):
                pos_x   = i*texture_dim - texture_dim/2
                pos_y   = j*texture_dim - texture_dim/2
                if xmin < pos_x < xmax and ymin < pos_y < ymax:
                    screen.blit(self.textures[self.texture_grid[i][j]-1],
                                (player.rect.x + (pos_x - player.level_pos_x),
                                 player.rect.y + (pos_y - player.level_pos_y)))
