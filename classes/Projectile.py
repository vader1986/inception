#---------------------------------------------------+
# Projectiles are fired when someone (player or
# villain) fires a shot with a gun.
# A projectile is basically a moving item.
#---------------------------------------------------+
import pygame, math

class Projectile(pygame.sprite.Sprite):

    origin      = []    # A vector representing x-y-coordinates: At which position in the level was the projectile generated
    speed       = 5     # Speed of the projectile
    max_range   = 10    # Maximum range of the projectile - defined by weapon used
    dmg         = 0     # Damage associated with the projectile
    position    = []    # Current level position
    angle       = 0     # Shooting direction

    def __init__(self, lvl):

        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites

        self.origin         = lvl.player.position
        self.angle          = lvl.player.angle
        # Postion the projectile a bit outside of the origin
#        v = (math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180))
#        new_x               = self.origin[0] + v[0] * 0.1
#        new_y               = self.origin[1] + v[1] * 0.1
#        self.origin         = [new_x, new_y]
        self.position       = self.origin

        current_weapon      = lvl.player.get_current_weapon()
        self.speed          = current_weapon.speed
        self.max_range      = current_weapon.max_range
        self.dmg            = current_weapon.generate_dmg_fun()
        # Get the right image for this sprite (based on level theme and weapon)
        self.image          = lvl.all_images[current_weapon.name + "_projectile"]
        self.image          = pygame.transform.rotate(self.image, -self.angle)
        self.rect           = self.image.get_rect()

    # Move the projectile (cannot change direction)
    def move_me(self):
        v = (math.cos(self.angle * math.pi / 180), math.sin(self.angle * math.pi / 180))
        new_pos_x = self.position[0] + v[0] * self.speed
        new_pos_y = self.position[1] + v[1] * self.speed
        if math.sqrt((new_pos_x - self.origin[0])**2+(new_pos_y-self.origin[1])**2) < self.max_range:
            self.position = [new_pos_x, new_pos_y]
        else:
            print "Out of range!"
            self.kill()