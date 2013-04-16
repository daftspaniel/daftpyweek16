import pygame
from pygame.locals import *
import random

class DroneWing(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0) ):
        pygame.sprite.Sprite.__init__(self)
        self.shipimgs = [pygame.image.load("img/shortwing1.png")]
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
        #self.shipswap += 1
        if self.rect.left<0: self.kill()
        #if self.shipswap==7:
        #    self.image = self.shipimgs[random.randrange(0, 2)]
        #    self.shipswap = 0

        
class BadBullet(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0) ):
        pygame.sprite.Sprite.__init__(self)
        
        self.shipimg = pygame.image.load("img/badbullet.png")
        self.image = self.shipimg
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.vmove = 0
        self.hmove = -8
                
    def update(self):
        self.rect.left += self.hmove
        if self.rect.left>640: self.kill()
