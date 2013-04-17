import pygame
from pygame.locals import *
import random

class DroneTower(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), imgs = [] ):
        pygame.sprite.Sprite.__init__(self)
        self.shipimgs = imgs
        self.hmove = -1
        self.image = self.shipimgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 40
        self.Damage = 40
        
    def update(self):
        self.rect.left += self.hmove
        self.shipswap += 1
        if self.rect.left<0: self.kill()
        if self.shipswap==7:
            self.image = self.shipimgs[random.randrange(0, 2)]
            self.shipswap = 0
