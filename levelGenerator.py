import pygame
from pygame.locals import *

from droneShip import DroneShip
from droneCrate import DroneCrate

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
        self.GameCore = None
        
    def Prepare(self, levelID):
        pass
        
    def Progress(self):
        """
            Add Objects as the player progresses.
        """
        
        gc = self.GameCore
        
        hund = gc.Step % 100 == 0 # 100th step
        
        if not hund: return
        
        if gc.Step==100:
            
            self.add_DroneShip( (640,240) )
            self.add_DroneShip( (640,180) )
            
            for x in range(0,4):
                self.add_Crate( (640, 384 - (32*x)) )
                self.add_Crate( (640, 32 - (32*x)) )
            for x in range(10):
                self.add_Crate( (704 + (32*x), 160) )
                self.add_Crate( (704 + (384*x), 160) )

    def add_DroneShip(self, pos):
        ds = DroneShip(pos, self.GameCore.DroneShipImgs)
        self.GameCore.BadGuys.add( ds )
        return ds
        
    def add_Crate(self, pos):
        ds =  DroneCrate(pos, self.GameCore.DroneCrateImgs)
        self.GameCore.BadGuys.add( ds )
        return ds
        
    def Draw(self, step, surface):
        """
            Draw Level - star field and borders
        """
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
