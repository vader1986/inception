#---------------------------------------------------------+
# React to user input (keyboard/joystick)
#---------------------------------------------------------+
import pygame
import Constants

#---------------------------------------------------------+
# Function to react to user input.
# Turns the player around, shoots, jumps, moves,...
# Returns true if player is moving, false when player stops
# moving.
#---------------------------------------------------------+
def listen(event, menu, lvl, game_state):
    pressed = pygame.key.get_pressed()
    if game_state == "main_menu":
        if event.type == pygame.KEYDOWN:
            if pressed[Constants.up]:
                menu.select_(False)
            if pressed[Constants.down]:
                menu.select_(True)
    elif game_state == "play_level":
        if pressed[Constants.left]:
            lvl.player.turn(-Constants.player_default_turn_speed)
        if pressed[Constants.right]:
            lvl.player.turn(Constants.player_default_turn_speed)
        if pressed[Constants.up]:
            lvl.player.move(1, lvl)
        if pressed[Constants.down]:
            lvl.player.move(-1, lvl)
        if pressed[pygame.K_w]: # DEBUGING
            for i in lvl.chars:
                print "Hpt: " + str(i.hitpoints[0])
        if event.type == pygame.KEYDOWN: # No constant fire
            if pressed[Constants.fire]:
                lvl.char_fire(lvl.player) # Let player fire
