import pygame
from pygame.locals import *

import random
clock = pygame.time.Clock()

# Libraries
#from levels import *
from playerShip import GoodShip

class Game(object):
    """ Nemesis Game """
    def __init__(self, surface):
        self.Surface = surface
        self.Playing = True
        
        # Player
        self.GoodGuy = GoodShip(self, (0,300))
        self.PlayerGroup = pygame.sprite.GroupSingle(self.GoodGuy)
        self.GoodBullets = []
        
    def Run(self):
        
        hmove = 0
        vmove = 0
        
        while self.Playing:
            time = clock.tick(50)
            
            self.PlayerGroup.update()
            
            self.Surface.fill((0, 0, 0))
            
            # Draw Level
            pygame.draw.rect(self.Surface, pygame.Color("yellow"), Rect(0, 450, 640,480), 0)
            
            # Draw Player
            self.PlayerGroup.draw(self.Surface)
            
            # Handle Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    print "keydown"
                    if event.key == K_q:
                        self.Playing = False
                        print "quit already!"
                        return
                    
                    keystate = pygame.key.get_pressed()
                    
                    if keystate[K_a]==1:
                        hmove = -1
                    elif keystate[K_d]==1:
                        hmove = 1
                    
                    if keystate[K_w]==1:
                        vmove = -1
                    elif keystate[K_s]==1:
                        vmove = 1
                        
                elif event.type == pygame.KEYUP:
                    keystate = pygame.key.get_pressed()

                    if keystate[K_a]==0:
                        hmove = 0
                    if keystate[K_d]==0:
                        hmove = 0
                    if keystate[K_w]==0:
                        vmove = 0
            self.GoodGuy.hmove = hmove
            self.GoodGuy.vmove = vmove
            print hmove, vmove
            # Refresh Display
            pygame.display.flip()
