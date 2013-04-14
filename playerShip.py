import pygame
from pygame.locals import *

class GoodShip(pygame.sprite.Sprite):
    
    def __init__(self, game, pos = (0,0) ):
        pygame.sprite.Sprite.__init__(self)
        
        self.shipimg = pygame.image.load("img/ship1.png")
        self.shipimgtilt = pygame.image.load("img/ship2.png")
        self.image = self.shipimg
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.image.set_colorkey(self.shipimg.get_at((0,0)), RLEACCEL)
        
        self.vmove = 0
        self.hmove = 0
        
    def update(self):
        
        if self.vmove!=0:
            self.rect.top += self.vmove * 3
            if self.vmove<0:
                self.image = self.shipimgtilt
            else:
                self.image = self.shipimgtilt
        else:
            self.image = self.shipimg
            
        if self.hmove!=0:
            self.rect.left += self.hmove * 2
