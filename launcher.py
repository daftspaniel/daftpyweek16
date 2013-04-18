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
pygame.mixer.init()
screen = sgc.surface.Screen((640, 480), DOUBLEBUF)
clock = pygame.time.Clock()

def main():
    
    menu = MenuScreen()
    
    while True:
        while menu.Active:
            game = Game(screen.image)
            menu.Run()
            game.Playing = True
        while game.Playing:
            game.Run()
            menu.Active = True

if __name__ == "__main__":
    main()
