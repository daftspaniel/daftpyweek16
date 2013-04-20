# Libraries
import pygame
from pygame.locals import *
import pygame.time
import random

import sgc
from sgc.locals import *

from animExplosion import Explosion

class MenuScreen(object):
    def __init__(self, screen):
        self.Active = True
        
        sgc.Menu.startgame = self.startgame
        sgc.Menu.exitgame = self.exitgame
        sgc.Menu.func_dict = lambda self: {"start": self.startgame,
                               "exit": self.exitgame}
        self.menu = sgc.Menu(menu=open("nemesismenu"))
        self.menu.add()
        self.clock = pygame.time.Clock()
        self.Screen = screen
        self.shipimg = pygame.image.load("img/newplayer0.png")
        self.grndimg = pygame.image.load("img/title.png")
        self.helpimgs = [pygame.image.load("img/mst4.png"),pygame.image.load("img/mst0.png"),pygame.image.load("img/mst1.png"),pygame.image.load("img/mst2.png"),pygame.image.load("img/mst3.png")]
        self.helpidx = 0
        self.shippos = (-10, 400)
        self.Explosions = []
        self.FullScreen = False
        pygame.mixer.music.load("menu.mp3")
        
        
    def startgame(self):
        self.Active = False
        
    def exitgame(self):
        exit()
        
    def Run(self):
        pygame.mixer.music.play(-1)
        
        while self.Active:
            time = self.clock.tick(40)
            
            if self.shippos[0]+2>735:
                self.shippos = (-10, 400)
                self.helpidx += 1
                if self.helpidx==len(self.helpimgs): self.helpidx = 0
            self.shippos = (self.shippos[0]+2, self.shippos[1])
            
            #if random.randrange(0,15)>10:
            #    self.Explosions.append(Explosion( (random.randrange(0,639), random.randrange(0,450)), random.randrange(15,65)))
            #print len(self.Explosions)
            
            for event in pygame.event.get():
                sgc.event(event)
                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_j]==1:
                        self.startgame()
                    if keystate[K_q]==1:
                        self.exitgame()
                    elif keystate[K_F11]==1:
                        self.FullScreen = not self.FullScreen
                        if self.FullScreen:
                            window = pygame.display.set_mode(self.ScreenSize, FULLSCREEN)
                        else:
                            window = pygame.display.set_mode(self.ScreenSize)
                if event.type == GUI:
                    pass
                elif event.type == QUIT:
                    exit()
            
            #self.background = pygame.Surface(self.Screen.get_size())
            
            #self.background = self.background.convert()
            
            #for e in self.Explosions:
            #    e.Draw(self.background)
            
            #self.Screen.blit(self.background, (0,0))
            sgc.update(time)
            #for e in self.Explosions:
            #    e.Update()
            #self.Explosions = [e for e in self.Explosions if e.Alive]
            
            self.Screen.blit(self.shipimg, self.shippos)
            self.Screen.blit(self.helpimgs[self.helpidx], (self.shippos[0]-193, self.shippos[1]) )
            self.Screen.blit(self.grndimg, (0,448))
            
            pygame.display.flip()
        pygame.mixer.music.stop()
