# Libraries
import pygame
from pygame.locals import *

import sgc
from sgc.locals import *

# Game Specific
from gameMenu import MenuScreen
from gameCore import Game

# Init
pygame.font.init()
pygame.display.init()

screen = sgc.surface.Screen((800,600))
clock = pygame.time.Clock()

def main():
    
    menu = MenuScreen()
    game = Game(screen.image)
    
    while True:
        while menu.Active:
            menu.Run()
            game.Playing = True
        while game.Playing:
            game.Run()
            menu.Active = True

if __name__ == "__main__":
    main()
