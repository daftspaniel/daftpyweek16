import pygame
from pygame.locals import *
import random

class DroneWalker(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), imgs = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Name = "Walker"
        self.shipimgs = imgs
        self.hmove = -2
        self.vmove = 0
        self.image = self.shipimgs[0]
        self.shipswap = 1
        self.curimg = 1
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 20
        self.Damage = 25
        self.HitsToDie = 2
        
        self.reload = 0
        self.firing = False
        
    def update(self):
        
        if self.firing:
            self.reload += 1
            if self.reload % 40 == 0:
                b = self.gameCore.AddBadBullet(self.rect.topleft)
                b.hmove = 0
                b.vmove = -2
                
        self.rect.left += self.hmove
        self.rect.top += self.vmove
        self.shipswap += 1
        
        if self.rect.left<0: self.kill()
        if self.shipswap==7:
            self.curimg += 1
            if self.curimg>9:
                self.curimg = 1
            self.image = self.shipimgs[self.curimg-1]
            self.shipswap = 1
