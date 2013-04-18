import pygame
from pygame.locals import *
import random

class DroneCrate(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), imgs = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Name = "Crate"
        self.hmove = -1
        self.vmove = 0
        self.image = imgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 1000
        self.Damage = 40
        self.HitsToDie = 1000
        
    def update(self):
        self.rect.left += self.hmove
        self.rect.top += self.vmove
        if self.rect.left<-self.rect.width: self.kill()
