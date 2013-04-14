import random
import pygame
import sys
from pygame.locals import *

class starField(object):
    def __init__(self, pos , size, max, speed):
        self.stars = []
        self.pos = pos
        self.size = size
        self.max = max
        self.speed = -speed
        self.box = True
        self.color = (155,155,155)
        self.bordercolor = Color(255,255,255)
        self.backgroundcolor = Color(0,0,0)
        for loop in range(0, max):
            star = [random.randrange(0, size[0] - 1),
                    random.randrange(0, size[1] - 1)]
            self.stars.append(star);
    def draw(self, screen):
        for loop in range(0, self.max):
            p = (self.pos[0] + self.stars[loop][0], self.pos[1] + self.stars[loop][1] )
            screen.set_at(p, self.color)
            
    def update(self):
        for loop in range(0, self.max):
            self.stars[loop] = (self.stars[loop][0] + self.speed, self.stars[loop][1])
            if self.stars[loop][0]<0:
                self.stars[loop] = (649, self.stars[loop][1])

