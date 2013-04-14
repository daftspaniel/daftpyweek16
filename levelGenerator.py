import pygame
from pygame.locals import *

from starField import starField

class Levels(object):
    def __init__(self, ID):
        self.Levels = []
        self.Borders = [pygame.image.load("img/grille.png")]
        self.Current = ID
        self.Stars = [starField( (0,32), (640,408), 20, 1 ), 
                      starField( (0,32), (640,408), 10, 2 ),
                      starField( (0,32), (640,408), 6, 3 )]
        
    def Prepare(self, levelID):
        pass
    
    def Draw(self, step, surface):
        
        surface.fill(pygame.Color("black"))
        
        for layer in self.Stars:
            if step % 4 == 1: layer.update()
            layer.draw(surface)
        r = self.Borders[0].get_rect()
        bwidth = r.width
        bheight = r.height
        step = (step % bwidth) * -1
        lb = 480 - (bheight*2)
        
        for x in range(21):
            bx = step + x*bwidth
            surface.blit(self.Borders[0], (bx,0))
            #surface.blit(self.Borders[0], (bx,lb))
        surface.blit(surface, (0,416), Rect(0,0,640,31))
