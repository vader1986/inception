#-------------------------------------+
# Main menu class
#-------------------------------------+
import pygame

import Constants


class Main_Menu(object):

    # Constructor
    def __init__(self, menu_items, active_img, passive_img):
        self.menu_items     = menu_items    # A list of menu items to be rendered
        self.selected       = 0             # Which of the items is selected
        self.imgs           = [active_img, passive_img]

    # Function to render the menu
    def render_menu(self, screen, screen_w, screen_h, margin):
        nitems  = len(self.menu_items)
        item_w  = screen_w * 3/5
        item_h  = (screen_h - (nitems+1)*margin)/nitems

        for i in range(0, nitems):
            if i == self.selected:
                self.menu_items[i].image = pygame.transform.scale(self.imgs[0], (item_w, item_h))
            else:
                self.menu_items[i].image = pygame.transform.scale(self.imgs[1], (item_w, item_h))

            self.menu_items[i].rect = self.menu_items[i].image.get_rect

            #--------------------------------------------------+
            # Render button image
            #--------------------------------------------------+
            screen.blit(self.menu_items[i].image, (screen_w/2 - item_w/2, 0 + margin + i*(margin + item_h)))

            #--------------------------------------------------+
            # Render text
            #--------------------------------------------------+
            itemText = Constants.menuFont.render(self.menu_items[i].text, True, Constants.BLACK)
            screen.blit(itemText, (screen_w/2 - itemText.get_width()/2, 0 + margin + i * (margin + item_h) + item_h/2 - itemText.get_height()/2))

    # Select next or previous menu item
    def select_(self, next):
        if next:
            if (self.selected+1) < len(self.menu_items):
                self.selected+=1
            else:
                self.selected=0
        else:
            if self.selected == 0:
                self.selected = len(self.menu_items)-1
            else:
                self.selected-=1