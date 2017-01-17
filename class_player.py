'''
    Player class. A character that is controlled by the player.
    Has some additional abilities like an inventory compared to
    character class.
'''
import class_character, math, funcs, pygame

class Player(class_character.Character):

    inventory = []  # A List containing all available weapons
    equiped_weapon = -1  # Id number which weapon is active

    def __init__(self, theme, maxhitpoints, hitpoints, speed):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.maxhitpoints           = maxhitpoints
        self.hitpoints              = hitpoints
        self.speed                  = speed
        self.theme                  = theme
        self.sound_fire             = funcs.load_sound("sounds/"     + theme + "/player/shot.ogg")
        self.sound_change_weapon    = funcs.load_sound("sounds/"     + theme + "/player/change_weapon.ogg")
        self.image                  = funcs.load_img("imgs/"         + theme + "/player/player.gif")
#        self.image                  = pygame.transform.scale(self.image, (24,24)) ==> Add player size to game?
        self.base_img               = self.image
        self.rect                   = self.image.get_rect()
        # Starting position in the level (might by changed during level initialization)
        self.level_pos_x            = 0
        self.level_pos_y            = 0

    # fire a shot
    def fire(self):
        if self.equiped_weapon == - 1:
            print "I don't have a weapon! :-("
            return None
        else:
            v       = [math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180)]
            shot    = self.inventory[self.equiped_weapon].generateProjectile(self.theme,
                                                                             self.rect.x + v[0],
                                                                             self.rect.y + v[1],
                                                                             self.angle)
            self.sound_fire.play() # Play sound when shooting
            return shot

    # Add a weapon to the inventory and make it the currently used weapon
    def add_weapon(self, weapon):
        self.inventory.append(weapon)
        self.equiped_weapon = len(self.inventory)-1
        print "Using " + weapon.name + " now."

    # Change the used weapon (direction is 1 for next weapon, -1 for previous weapon)
    def next_weapon(self, direction):
        if direction == 1: # Next weapon
            if self.equiped_weapon+1 > len(self.inventory)-1: # If you are already using the last weapon in inv go to first
                self.equiped_weapon = 0
            else: # Next weapon
                self.equiped_weapon+=1
        else:
            if self.equiped_weapon-1 < 0: # If you are already using the first weapon => take last
                self.equiped_weapon = len(self.inventory)-1
            else: # Previous weapon
                self.equiped_weapon-=1
        print "Using " + self.inventory[self.equiped_weapon].name + " now."
        self.sound_change_weapon.play() # Play sound change weapon

    # When character is hit by a projectile
    def get_hit(self, dmg):
        self.hitpoints-=dmg
        if self.hitpoints <=0:
            self.rect.x = -100
            self.rect.y = -100
            pygame.sprite.Sprite.kill(self)
            print "Buhuuuu"