
import pygame
from pygame.locals import *

class ShieldBoost(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), imgs = [] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.imgs = imgs
        self.image = self.imgs[0]
        self.imgswap = 0
        self.curimg = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.vmove = 0
        self.hmove = -1
        self.Health = 20
        
    def update(self):
        self.rect.left += self.hmove
        if self.rect.left>740 or self.rect.left<0: self.kill()
        
        self.imgswap += 1
        
        if self.imgswap==7:
            self.curimg += 1
            if self.curimg>6: self.curimg = 0 
            self.image = self.imgs[self.curimg]
            self.imgswap = 0
