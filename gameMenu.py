# Libraries
import pygame
from pygame.locals import *
import pygame.time

import sgc
from sgc.locals import *

class MenuScreen(object):
    def __init__(self):
        self.Active = True
        
        sgc.Menu.startgame = self.startgame
        sgc.Menu.exitgame = self.exitgame
        sgc.Menu.func_dict = lambda self: {"start": self.startgame,
                               "exit": self.exitgame}
        self.menu = sgc.Menu(menu=open("nemesismenu"))
        self.menu.add()
        self.clock = pygame.time.Clock()
        
    def startgame(self):
        self.Active = False
    def exitgame(self):
        exit()
    def Run(self):
        while self.Active:
            time = self.clock.tick(30)
            for event in pygame.event.get():
                sgc.event(event)
                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_j]==1:
                        self.startgame()
                if event.type == GUI:
                    pass
                elif event.type == QUIT:
                    exit()
            
            sgc.update(time)
            pygame.display.flip()
