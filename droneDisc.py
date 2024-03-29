import pygame
from pygame.locals import *
import random

class DroneDisc(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), imgs = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Name = "Disc"
        self.shipimgs = imgs
        self.hmove = -4
        self.vmove = -4
        self.image = self.shipimgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 10
        self.Damage = 20
        self.HitsToDie = 1
        
    def update(self):
        
        self.rect.left += self.hmove
        self.rect.top += self.vmove
        #self.shipswap += 1
        
        if self.rect.left<0: self.hmove = 4
        if self.rect.left>640: self.hmove = -4
        
        if self.rect.top>416: self.vmove = -4
        if self.rect.top<32: self.vmove = 4
        
        #if self.shipswap==7:
        #    self.image = self.shipimgs[random.randrange(0, 2)]
        #    self.shipswap = 0
