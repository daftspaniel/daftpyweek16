import pygame
from pygame.locals import *

from droneShip import DroneShip
from droneCrate import DroneCrate
from droneWing import DroneWing
from droneWalker import DroneWalker
from droneTower import DroneTower
from droneSnakehead import DroneSnakeHead

from niceThings import ShieldBoost
from starField import starField

class Levels(object):
    def __init__(self, ID):
        self.Levels = []
        self.Borders = [pygame.image.load("img/grille.png"), pygame.image.load("img/lava.png"), pygame.image.load("img/iceb.png") ]
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
            
            for x in range(0,4):
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
            self.add_ShieldBoost()
            
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
            self.Text = "Super Shooting!"
        
        elif gc.Step==3100:
            self.Text = "Onto Level 2"
            self.Current = 2
        
        elif gc.Step==3200:
            
            self.Text = None
            for x in range(1,5):
                self.add_DroneHomingShip( (540 + (x*100), 20) )
                
        elif gc.Step==3600:
            
            self.add_CrateHill(4)
            
        elif gc.Step==3900:
            
            self.add_CrateHill(3)
        
        elif gc.Step==4000:
        
            for x in range(0,8):
                m = (32*x)
                self.add_DroneShip( (640, 64 + m) )
        
        elif gc.Step==4300:
            
            self.add_DroneTower((670, 344))
            #self.add_DroneTower((705, 344))
            
            self.add_DroneHomingShip( (-40, 0) )
            self.add_DroneHomingShip( (-140, 400) )
            #self.add_DroneHomingShip( (740, 0) )
            #self.add_DroneHomingShip( (740, 400) )
            
            self.add_DroneWing( (710, 250) )
            
        elif gc.Step==4500:
            
            self.add_CrateHill(8)
            
        elif gc.Step==5200:
            
            self.add_DroneWing( (640, 120) )
            self.add_DroneWing( (640, 220) )
            self.add_DroneWing( (640, 320) )

            self.add_DroneWing( (840, 120) )
            self.add_DroneWing( (840, 220) )
            self.add_DroneWing( (840, 320) )
            
            self.add_DroneWing( (1040, 120) )
            self.add_DroneWing( (1040, 220) )
            self.add_DroneWing( (1040, 320) )
    
        elif gc.Step==5600:
            
            self.add_DroneTower((670, 344))
            self.add_DroneTower((720, 344))
            self.add_DroneTower((770, 344))
            self.add_DroneTower((820, 344))
            
        elif gc.Step==6000:
            
            self.add_ShieldBoost()
            
        elif gc.Step==6100:
            
            self.Text = None
            
        elif gc.Step==6400:
            self.Text = "Born To Zap!"
        
        elif gc.Step==6500:
            self.Text = "Onto Level 3"
            self.Current = 3
        
        elif gc.Step==6600:
            self.Text = None
            
            for x in range(0,10):
                m = (32*x)
                self.add_Crate( (640, 64 + m) )
            
            for x in range(0,10):
                m = (32*x)
                self.add_Crate( (1040, 64 + m) )
            
        elif gc.Step==7500:
            
            self.add_DroneSnake( (640,230) )
            self.add_CrateUpHill(4)
            
        elif gc.Step==8000:
            
            self.add_DroneWalker( (640,384) )
            self.add_DroneWalker( (840,384) )
            self.add_DroneWalker( (1040,384) )
            self.add_DroneWalker( (1240,384) )
        
        elif gc.Step==8300:
            
            self.add_CrateHill(4)
            
            self.add_CrateUpHill(4)
        
            self.add_DroneWing( (640, 120) )
            self.add_DroneWing( (640, 220) )
            self.add_DroneWing( (640, 320) )

        elif gc.Step==8500:
            
            self.add_CrateHill(9)
            
            self.add_DroneWing( (640, 120) )
            self.add_DroneWing( (640, 220) )
            self.add_DroneWing( (640, 320) )
            
        elif gc.Step==8900:
            
            self.add_CrateUpHill(9)
            
            self.add_DroneWing( (640, 120) )
            self.add_DroneWing( (640, 220) )
            self.add_DroneWing( (640, 320) )
            
            d = self.add_DroneWalker( (640,384) )
            d.firing = True
            d = self.add_DroneWalker( (840,384) )
            d.firing = True
            
        elif gc.Step==9400:
            
            self.add_DroneShip( (640, 348) )
            self.add_DroneShip( (740, 348) )
            self.add_DroneShip( (840, 348) )
        
        elif gc.Step==9700:
            
            self.add_FlippedWalker((840,32))
            self.add_FlippedWalker((1040,32))
            
            self.add_ShieldBoo( (640, 208) )
            
            #self.add_DroneTower((670, 344))
            self.add_DroneTower((720, 344))
            self.add_DroneTower((870, 344))
            
            self.add_DroneSnake( (640,230) )
            
        elif gc.Step==10200:
            self.Text = "The Drones Are Getting Scared!"
        
        elif gc.Step==10300:
            self.Text = "Onto Level 4"
            self.Current = 4
            
        elif gc.Step==10400:
            self.Text = None
            self.add_ShieldBoost()
            
    def add_FlippedWalker(self, pos):
        d = self.add_DroneWalker( pos )
        d.firing = True
        d.Flip()
        
    def add_DroneSnake(self, pos):
        dsh = DroneSnakeHead((pos[0], pos[1]), self.GameCore.SnakeheadImgs)
        dsh.gameCore = self.GameCore
        dsh.CanFire = True
        self.GameCore.BadGuys.add( dsh )
        
        ds = DroneSnakeHead((pos[0] + 32, pos[1]), self.GameCore.SnakebodyImgs)
        ds.gameCore = self.GameCore
        ds.hlimit += 32
        self.GameCore.BadGuys.add( ds )
        dsh.Tail.append(ds)
        
        ds = DroneSnakeHead((pos[0] + 64, pos[1]), self.GameCore.SnakebodyImgs)
        ds.gameCore = self.GameCore
        ds.hlimit += 64
        self.GameCore.BadGuys.add( ds )
        dsh.Tail.append(ds)
        
        ds = DroneSnakeHead((pos[0] + 96, pos[1]), self.GameCore.SnaketailImgs)
        ds.gameCore = self.GameCore
        ds.hlimit += 96
        self.GameCore.BadGuys.add( ds )
        dsh.Tail.append(ds)
        
    def add_ShieldBoost(self):
        
            self.Text = "50% Shield Boost - Get It!"
            
            # Special Bonus
            droneshield = [(640, 208),(672, 256), (672, 160), (704, 208)]
            for p in droneshield:
                ds = self.add_DroneShip(p)
                ds.hmove = -1
            sb = self.add_ShieldBoo( (672+4, 208+4) )
            sb.Health = 50
            sb.hmove = -1
            
    def add_CrateHill(self, peak):
        
        for x in range(0,peak):
            m = (32*x)
            mx = 640 + m
            my = 384 - m
            self.add_Crate( (mx, my ) )
            
        mx -= 32
        my -= 32
        
        for x in range(0,peak):
            mx += 32
            my += 32
            self.add_Crate( (mx,my) )
        
    def add_CrateUpHill(self, peak):
        
        for x in range(0,peak):
            m = (32*x)
            mx = 640 + m
            my = 384 - m
            self.add_Crate( (mx, 416- my ) )
            
        mx -= 32
        my -= 32
        
        for x in range(0,peak):
            mx += 32
            my += 32
            self.add_Crate( (mx,416-  my) )
    
    def add_DroneTower(self, pos):
        dt = DroneTower(pos, self.GameCore.TowerImgs)
        self.GameCore.BadGuys.add( dt )
        dt.gameCore = self.GameCore
        return dt
        
    def add_ShieldBoo(self, pos):
        sb = ShieldBoost(pos, self.GameCore.ShieldBoostImgs)
        self.GameCore.Bonuses.add(sb)
        return sb

    def add_DroneHomingShip(self, pos):
        ds = self.add_DroneWing( pos )
        ds.targetvert = self.GameCore.GoodGuy.rect.midright[1]
        self.GameCore.BadGuys.add( ds )
        return ds
        
    def add_DroneShip(self, pos):
        ds = DroneShip(pos, self.GameCore.DroneShipImgs)
        self.GameCore.BadGuys.add( ds )
        return ds
        
    def add_DroneWalker(self, pos):
        ds = DroneWalker(pos, self.GameCore.DroneWalkerImgs)
        self.GameCore.BadGuys.add( ds )
        ds.gameCore = self.GameCore
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
        
        if step>6500:
            self.ActiveBorder = 2
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
