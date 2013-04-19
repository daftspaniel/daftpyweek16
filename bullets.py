import pygame
from pygame.locals import *
import random

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
        self.rect.top += self.vmove
        if self.rect.left>640 or self.rect.left<0: self.kill()

class GoodBullet(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0), img =[] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img[0]
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.vmove = 0
        self.hmove = 8
                
    def update(self):
        self.rect.left += self.hmove
        self.rect.top += self.vmove
        if self.rect.left>631 or self.rect.left<0: self.kill()
