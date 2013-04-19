import pygame
from pygame.locals import *
import random

class DroneTower(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), imgs = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Name = "Tower"
        self.imgs = imgs
        self.hmove = -1
        self.image = self.imgs[0]
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 40
        self.Damage = 50
        self.reload = 0
        self.HitsToDie = 12
        self.firing = False
        
    def update(self):
        if self.firing:
            self.reload += 1
            if self.reload % 10 == 0:
                b = self.gameCore.AddBadBullet(self.rect.topleft)
                b.vmove = b.hmove
                
        if self.rect.left<600  and  self.rect.left>550:
            self.image = self.imgs[1]
        elif self.rect.left<551:
            self.image = self.imgs[2]
            self.firing = True
        self.rect.left += self.hmove
        if self.rect.left<-30: self.kill()
