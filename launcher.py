# Libraries
import pygame
from pygame.locals import *

import sgc
from sgc.locals import *

# Game Specific
from gameMenu import MenuScreen


# Init
pygame.font.init()
pygame.display.init()

screen = sgc.surface.Screen((800,600))
clock = pygame.time.Clock()

def main():
    
    menu = MenuScreen()
    
    #while True:
    while menu.Active:
        menu.Run()
        #    g.Playing = True
        #while g.Playing:
        #    print "play"

if __name__ == "__main__":
    main()
