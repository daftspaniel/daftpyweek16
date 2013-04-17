import pygame
from pygame.locals import *
import random

class DroneWing(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), img = [] ):
        pygame.sprite.Sprite.__init__(self)
        self.shipimgs = img
        self.hmove = -4
        self.image = self.shipimgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 20
        self.Damage = 30
        
    def update(self):
        self.rect.left += self.hmove
        if self.rect.left<0: self.kill()

class BadBullet(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), img =[] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img[0]
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.vmove = 0
        self.hmove = -8
                
    def update(self):
        self.rect.left += self.hmove
        if self.rect.left>640: self.kill()
