import pygame
from pygame.locals import *

class Levels(object):
    def __init__(self, ID):
        self.Levels = []
        self.Borders = [pygame.image.load("img/grille.png")]
        self.Current = ID
    def Prepare(self, levelID):
        pass
    
    def Draw(self, step, surface):
        
        surface.fill(pygame.Color("black"))
        r = self.Borders[0].get_rect()
        bwidth = r.width
        bheight = r.height
        step = (step % bwidth) * -1
        lb = 480 - (bheight*2)
        
        for x in range(21):
            bx = step + x*bwidth
            surface.blit(self.Borders[0], (bx,0))
            surface.blit(self.Borders[0], (bx,lb))
