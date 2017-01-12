'''
    The game's level class.

    A level contains information about:
    - The graphics/sound theme that is used
    - Dimension of the map
    - Location of Start and Goal
    - Location ob obstacles

'''
class Level:

    obstacles       = [] # A list of obstacles
    characters      = [] # A list of villians
    width           = 100  # Height in ?
    height          = 1000 # Width in ?

    def __init__(self):
        pass