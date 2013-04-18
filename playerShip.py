import pygame
from pygame.locals import *

class GoodShip(pygame.sprite.Sprite):
    
    def __init__(self, game, pos = (0,0) ):
        pygame.sprite.Sprite.__init__(self)
        
        self.shipimg = pygame.image.load("img/newplayer.png")
        self.shipimgtiltup = pygame.image.load("img/ship2.png")
        self.shipimgtiltdown = pygame.image.load("img/ship3.png")
        self.image = self.shipimg
        
        self.rect = self.image.get_rect()
        self.rect.top = pos[1]
        self.rect.left = pos[0]
        
        self.image.set_colorkey(self.shipimg.get_at((0,0)), RLEACCEL)
        
        self.vmove = 0
        self.hmove = 0
        self.fire = 0
        self.fired = 0
        self.bullets = []
        self.reload = 0
        self.ZapSound = pygame.mixer.Sound("zap.wav")
        
    def update(self):
        
        self.reload += 1
        
        # Fire!
        if self.fire and self.reload>4:
            self.ZapSound.play()
            self.fired = 1
            self.reload = 0
        else:
            self.fired = 0
        
        # Movement
        if self.vmove!=0:
            self.rect.top += self.vmove * 4
            if self.vmove<0:
                self.image = self.shipimgtiltup
            else:
                self.image = self.shipimgtiltdown
        else:
            self.image = self.shipimg
            
        if self.hmove!=0:
            self.rect.left += self.hmove * 2
        
        if self.rect.left>608: self.rect.left =608
        if self.rect.left<0: self.rect.left =0
        
        if self.rect.top>384: self.rect.top = 384
        if self.rect.top<32: self.rect.top = 32
        
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
        if self.rect.left>640: self.kill()
