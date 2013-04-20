import pygame

class Explosion(object):
    def __init__(self, pos, width):
        self.pos = pos
        self.gap = 1
        self.width = width
        self.Alive = True
        
    def Update(self):
        self.gap *= 2
        
    def Draw(self, screen):
        pos = self.pos
        width = self.width
        d = 0
        for l in range(2,12):
            m = self.gap * l
            if not pos[0]-m<33 or not pos[1]+m>416:
                d+=1
                if self.gap % 4 == 0:
                    ec = (255, 0, 0)
                else:
                    ec = (0, 0, 255)
                pygame.draw.line(screen, ec, (pos[0], pos[1]-m), (pos[0] + width, pos[1]-m))
                pygame.draw.line(screen, ec, (pos[0], pos[1]+m), (pos[0] + width, pos[1]+m))
                
                #pygame.draw.line(screen, (255, 0, 0), (pos[0], pos[1]), (pos[0], pos[1]) )
                #pygame.draw.line(screen, (255, 0, 0), (pos[0], pos[1]), (pos[0], pos[1]) )
        if d==0:
            self.Alive = False
