import pygame
from pygame.locals import *
import random

class DroneShip(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0) ):
        pygame.sprite.Sprite.__init__(self)
        self.shipimgs = [pygame.image.load("img/drone1.png"),
                         pygame.image.load("img/drone2.png"),
                         pygame.image.load("img/drone3.png")]
        self.hmove = -4
        self.image = self.shipimgs[0]
        self.shipswap = 0
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.ScoreValue = 10
        self.Damage = 20
        
    def update(self):
        self.rect.left += self.hmove
        self.shipswap += 1
        if self.rect.left<0: self.kill()
        if self.shipswap==7:
            self.image = self.shipimgs[random.randrange(0, 2)]
            self.shipswap = 0
