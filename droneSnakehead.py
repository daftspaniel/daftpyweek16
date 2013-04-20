import pygame
from pygame.locals import *
import random

class DroneSnakeHead(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), img = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Name = "SnakeHead"
        self.shipimgs = img
        self.hmove = -2
        self.vmove = 0
        self.image = self.shipimgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 200
        self.Damage = 102
        self.HitsToDie = 10
        self.reload = 0
        self.firing = False
        self.targetvert = -1
        self.hlimit = 400
        self.CanFire = False
        self.Tail = []
        
    def update(self):
        if self.CanFire and self.firing:
            self.reload += 1
            if self.reload % 10 == 0:
                b = self.gameCore.AddBadBullet(self.rect.midleft)
                #b.vmove = b.hmove
        
        if self.targetvert>-1:
        
            if abs(self.targetvert-self.rect.top)>10:
                if self.targetvert>self.rect.top:
                    self.vmove = 8
                else:
                    self.vmove = -8
            else:
                self.vmove = 0
        else:
            self.vmove = 0
        
        if len(self.Tail)==0 and random.randint(1,45)>40:
            self.vmove += (5 - random.randint(1,3))
        
        if self.rect.left<self.hlimit:
            self.hmove = 0
            self.firing = True

        self.rect.left += self.hmove
        self.rect.top += self.vmove
        if self.rect.left<0: self.kill()
        if self.rect.top>410: self.rect.top = 410
        self.Retarget()
        
    def Retarget(self):
        self.targetvert = self.gameCore.GoodGuy.rect.midright[1] + random.randint(16,32)


