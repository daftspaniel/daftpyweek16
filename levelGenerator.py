import pygame
from pygame.locals import *

from starField import starField

class Levels(object):
    def __init__(self, ID):
        self.Levels = []
        self.Borders = [pygame.image.load("img/grille.png"), pygame.image.load("img/lava.png")]
        self.Current = ID
        self.Stars = [starField( (0,32), (640,408), 18, 1 ), 
                      starField( (0,32), (640,408), 8, 2 ),
                      starField( (0,32), (640,408), 6, 3 )]
        self.rendback = None
        self.ActiveBorder = 1
        self.SideScroll = True
        
    def Prepare(self, levelID):
        pass
    
    def Draw(self, step, surface):
        
        if step>1000:
            self.ActiveBorder = 0
            self.rendback = None
        r = self.Borders[0].get_rect()
        bwidth = r.width
        bheight = r.height
        
        if not self.rendback:
            self.rendback = pygame.Surface((672, 32))
            for x in range(21):
                bx = x*bwidth
                self.rendback.blit(self.Borders[self.ActiveBorder], (bx,0))
        surface.fill(pygame.Color("black"))
        
        for layer in self.Stars:
            if step % 4 == 1 and self.SideScroll: layer.update()
            layer.draw(surface)
        
        if self.SideScroll:
            step = (step % bwidth) * -1
        else:
            step = 0
            
        lb = 480 - (bheight*2)
        
        surface.blit(self.rendback, (step,0))
        surface.blit(self.rendback, (step,lb))
