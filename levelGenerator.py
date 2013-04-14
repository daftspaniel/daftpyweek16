import pygame
from pygame.locals import *

class Levels(object):
    def __init__(self):
        self.Levels = []
        self.Borders = [pygame.image.load("img/grille.png")]
        
    def Prepare(self, levelID):
        pass
    
    def Draw(self, surface):
        
        surface.fill(pygame.Color("black"))
        r = self.Borders[0].get_rect()
        bwidth = r.width
        bheight = r.height
        
        for x in range(20):
            surface.blit(self.Borders[0], (x*bwidth,0))
            surface.blit(self.Borders[0], (x*bwidth,480-bheight))
