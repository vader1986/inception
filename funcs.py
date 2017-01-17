# All helper functions

# Libraries
import os, pygame, class_player, class_weapon, class_level, class_obstacle, random, math

# Params
# Colors
BLACK           = (  0,   0,   0)
WHITE           = (255, 255, 255)
RED             = (255,0,0)
# Screen size
screen_width    = 400
screen_height   = 300

# Default key bindings
up      = pygame.K_UP
down    = pygame.K_DOWN
left    = pygame.K_LEFT
right   = pygame.K_RIGHT
fire    = pygame.K_SPACE
next_w  = pygame.K_e
prev_w  = pygame.K_q

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

# Set up a list with all weapons
def generate_weapons():
    wpn = []
    # Weapon objects
    gun = class_weapon.Weapon("Gun",1,5,50,15)
    wpn.append(gun)
    rifle = class_weapon.Weapon("rifle",3,10,70,12)
    wpn.append(rifle)
    bazooka = class_weapon.Weapon("bazooka",10,20,80,10)
    wpn.append(bazooka)
    return wpn

# Move the player's position on the map
def move_player(player, level):
    v = (math.cos(player.angle * math.pi / 180), math.sin(player.angle * math.pi / 180))
    new_pos_x = player.level_pos_x + v[0] * player.speed
    new_pos_y = player.level_pos_y + v[1] * player.speed
    if 0 < new_pos_x < level.width and 0 < new_pos_y < level.height:
        player.level_pos_x += v[0] * player.speed
        player.level_pos_y += v[1] * player.speed
    else:
        print "bounce of the level wall"


# Draw the HUD
def draw_HUD(player, screen):
    # Get information about the screen (dimension)
    screen_info     = pygame.display.Info()

    # Draw a rectangle containing an img representing the currently used weapon
    border          = 12
    height          = 35
    width           = 35
    img             = load_img("imgs/" + player.theme + "/weapon/" + player.inventory[player.equiped_weapon].name + ".gif")
    img             = pygame.transform.scale(img, (width, height))
    img_rect        = img.get_rect()
    bg_img          = load_img("imgs/textures/light_penal.jpg")
    bg_img          = pygame.transform.scale(bg_img, (width+border, height+border))
    bg_img_rect     = bg_img.get_rect()
    x               = screen_info.current_w / 2 - width / 2
    y               = screen_info.current_h - height - border
    img_rect.x      = x
    img_rect.y      = y
    bg_img_rect.x   = x - border/2
    bg_img_rect.y   = y - border/2
    # Draw the stuff
    screen.blit(bg_img, bg_img_rect)
    screen.blit(img, img_rect)

# The game loop
def game_loop():

    # Initialize Pygame
    pygame.init()

    # Initial Parameters
    # Initial parameters for the movement control of the player in game loop
    turnleft = False
    turnright = False
    move = False
    # Load Fonts
    font = pygame.font.SysFont("arial", bold=True, size=12)

    # Set the height and width of the screen
    screen = pygame.display.set_mode([screen_width, screen_height])

    # List with all character sprites
    chars       = pygame.sprite.Group()
    shots       = pygame.sprite.Group()
    level_obs   = pygame.sprite.Group()


    '''---------------------------------------------------------------+
        Create dummy level for testing.
    '''
    lvl         = class_level.Level()
    lvl.set_screen(screen)
    lvl.height  = 620
    lvl.width   = 620
    lvl.generate_random_texture_grid(100,100)
    for i in range(10):
        obs = class_obstacle.Obstacle(random.randint(0, lvl.width), random.randint(0, lvl.height), [30, 35], "imgs/classic/obs/tree1.gif")
        lvl.add_obstacle(obs)
        level_obs.add(obs)
    '''
    End of level stuff
    ---------------------------------------------------------------+'''

    # Generate a list with weapons
    weapons = generate_weapons()

    # Create the player
    player = class_player.Player("classic", 100, 95, 5)

    # Position of the player on the screen
    player.rect.x = screen_width/2-6
    player.rect.y = screen_height/2

    player.level_pos_x = lvl.width/2
    player.level_pos_y = lvl.height/2

    for i in weapons: # Add all weapons to the players inventory
        player.add_weapon(i)

    chars.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ''' THE HUGE GAME LOOP! '''
    while not done:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # KEYBOARD
            # React to pressed keys
            if event.type == pygame.KEYDOWN:
                if event.key == left:
                    turnleft = True
                if event.key == right:
                    turnright = True
                if event.key == up:
                    move = True
                    player.speed = abs(player.speed)
                if event.key == down:
                    move = True
                    player.speed = -abs(player.speed)
                if event.key == fire:  # Fire a shot
                    shot = player.fire()
                    shots.add(shot)
                if event.key == prev_w:  # Change weapon
                    player.next_weapon(-1)
                if event.key == next_w:
                    player.next_weapon(1)
                if event.key == pygame.K_w: # DEBUG
                    print str(player.level_pos_x) + "/" + str(player.level_pos_y)
            # React to key released
            if event.type == pygame.KEYUP:
                if event.key == left:
                    turnleft = False
                if event.key == right:
                    turnright = False
                if event.key == up:
                    move = False
                if event.key == down:
                    move = False
        if move:
            move_player(player, lvl)
        if turnright:
            player.turn(5, "right")
        if turnleft:
            player.turn(5, "left")

        # Clear the screen
        screen.fill(BLACK)

        # Move all shots
        for i in shots:
            i.move()

        # Draw the level
        lvl.draw_textures(player, screen)
        lvl.draw_view(player, screen)

        # Draw to the screen
        chars.draw(screen)
        shots.draw(screen)


        # HUD: Print stats
        draw_HUD(player, screen)

        # 60 fps
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()


'''
 # Joystick control
        if pygame.joystick.get_count() > 0:
        pygame.joystick.init()
        js = pygame.joystick.Joystick(0)
        js.init()

 # JOYSTICK
            if event.type == pygame.JOYHATMOTION:
                evt = js.get_hat(0)
                if evt[0] == -1:  # left
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
                    turnright = False
                    turnleft = False
                if evt[1] == 0:
                    move = False
            if event.type == pygame.JOYBUTTONDOWN:
                evt = js.get_button(1)
                if evt == 1:
                    shot = player.fire()
                    shots.add(shot)

'''


''' CONTROLLING PLAYER ETC
 # control movement direction


            # Check for collusions of villians with projectiles
            #   villian_hits = pygame.sprite.spritecollide(villian, shots, True)
            #   if len(villian_hits) > 0:
            #       villian.get_hit(shot.dmg)
'''