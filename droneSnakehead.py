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
        
        self.ScoreValue = 20
        self.Damage = 30
        self.HitsToDie = 2
        self.reload = 0
        self.firing = False
        self.targetvert = -1
        
    def update(self):
        if self.firing:
            self.reload += 1
            if self.reload % 10 == 0:
                b = self.gameCore.AddBadBullet(self.rect.topleft)
                b.vmove = b.hmove
        
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
            
        if self.rect.left<400:
            self.hmove = 0
            self.firing = True

        self.rect.left += self.hmove
        self.rect.top += self.vmove
        if self.rect.left<0: self.kill()

        self.Retarget()
        
    def Retarget(self):
        self.targetvert = self.gameCore.GoodGuy.rect.midright[1]


