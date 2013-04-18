import pygame
from pygame.locals import *

from droneShip import DroneShip
from droneCrate import DroneCrate
from droneWing import DroneWing
from droneTower import DroneTower
from droneSnakehead import DroneSnakeHead

from niceThings import ShieldBoost
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
        self.Text = "Approaching..."
        
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
            
            self.Text = None
            self.add_DroneShip( (640,240) )
            self.add_DroneShip( (640,180) )
            self.add_DroneShip( (840,180) )
            self.add_DroneShip( (840,240) )
            
            for x in range(0,5):
                m = (32*x)
                self.add_Crate( (640 + m, 384 - m) )
                self.add_Crate( (640 + m, 32 + m) )
                
        elif gc.Step==700:
            
            self.add_DroneWing( (640, 220) )
            self.add_DroneShip( (640, 300) )
            
        elif gc.Step==900:
            
            for x in range(0,8):
                m = (32*x)
                self.add_DroneShip( (640, 384 - m) )
                self.add_DroneShip( (902, 64 + m) )
                
        elif gc.Step==1100:
            
            for x in range(0,10):
                m = (32*x)
                self.add_Crate( (640, 64 + m) )
            
            for x in range(0,10):
                m = (32*x)
                self.add_Crate( (1040, 64 + m) )
                
        elif gc.Step==1300:
            
            self.add_DroneWing( (640, 120) )
            self.add_DroneWing( (640, 320) )
            
        elif gc.Step==1400:
            
            self.add_DroneWing( (640, 220) )
            self.add_DroneWing( (640, 388) )
        
        elif gc.Step==2000:
            self.Text = "50% Shield Boost - Get It!"
            
            # Special Bonus
            droneshield = [(640, 208),(672, 256), (672, 160), (704, 208)]
            for p in droneshield:
                ds = self.add_DroneShip(p)
                ds.hmove = -1
            sb = self.add_ShieldBoo( (672+4, 208+4) )
            sb.Health = 50
            sb.hmove = -1
            
        elif gc.Step==2100:
            self.Text = None
            
        elif gc.Step==2300:
            
            for x in range(0,10):
                m = (32*x)
                self.add_DroneShip( (640, 64 + m) )
            
            self.add_DroneWing( (840, 220) )
            
            for x in range(0,10):
                m = (32*x)
                self.add_DroneShip( (1040, 64 + m) )
            
            self.add_DroneWing( (1240, 220) )
            
            for x in range(0,10):
                m = (32*x)
                self.add_DroneShip( (1440, 64 + m) )
                
        elif gc.Step==3000:
            self.Text = "Super Shooting - Onto Level 2"
            self.Current = 2
        
        elif gc.Step==3200:
            self.Text = None
            
    def add_ShieldBoo(self, pos):
        sb = ShieldBoost(pos, self.GameCore.ShieldBoostImgs)
        self.GameCore.Bonuses.add(sb)
        return sb

    def add_DroneShip(self, pos):
        ds = DroneShip(pos, self.GameCore.DroneShipImgs)
        self.GameCore.BadGuys.add( ds )
        return ds
        
    def add_DroneWing(self, pos):
        ds = DroneWing(pos, self.GameCore.DroneWingImgs)
        ds.gameCore = self.GameCore
        #ds.targetvert = self.GoodGuy.rect.midright[0]
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
        if step>3000:
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
