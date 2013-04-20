import pygame
from pygame.locals import *
import random

class DroneWing(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), img = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Name = "Wing"
        self.shipimgs = img
        self.hmove = -3
        self.vmove = 0
        self.image = self.shipimgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 20
        self.Damage = 30
        self.HitsToDie = 1
        self.reload = 0
        self.firing = False
        self.targetvert = -1
        
    def update(self):
        if self.firing:
            self.reload += 1
            if self.reload % 40 == 0:
                b = self.gameCore.AddBadBullet(self.rect.topleft)
                if self.targetvert>-1:self.Retarget()
        if self.targetvert>-1:
            if abs(self.targetvert-self.rect.top)>10:
                if self.targetvert>self.rect.top:
                    self.vmove = 8
                else:
                    self.vmove = -8
            else:
                self.vmove = 0
            if (self.rect.left<0 and self.hmove<0) or (self.rect.left>666 and self.hmove>0): 
                self.hmove *= -1
                self.Retarget()
        else:
            self.vmove = 0
        #print abs(self.targetvert-self.rect.top), self.targetvert, self.vmove, self.rect.top
        
        self.rect.left += self.hmove
        self.rect.top += self.vmove
        if self.rect.left<630:
            self.firing = True
            #self.kill()
    def Retarget(self):
        self.targetvert = self.gameCore.GoodGuy.rect.midright[1]
