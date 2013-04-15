import pygame
import pygame.sprite
from pygame.locals import *

import random
clock = pygame.time.Clock()

# Libraries
from levelGenerator import Levels
from playerShip import GoodShip, GoodBullet
from droneShip import DroneShip
from animExplosion import Explosion

class Game(object):
    """ Nemesis Game """
    def __init__(self, surface):
        
        self.Surface = surface
        self.Playing = True
        self.Font = pygame.font.Font("Geo-Regular.ttf",30)
        
        # Player
        self.GoodGuy = GoodShip(self, (0,300))
        self.PlayerGroup = pygame.sprite.GroupSingle(self.GoodGuy)
        self.GoodBullets = pygame.sprite.Group()
        self.Score = 0
        
        # Bad Guys
        self.BadGuys = pygame.sprite.Group()
        self.BadBullets = pygame.sprite.Group()
        
        # Items
        self.Explosions = []
        
        # Levels
        self.Level = Levels(0)
        self.SetLevel(0)
        
    def SetLevel(self, level):
        self.Step = 0
        self.LevelID = level
        
    def ProgressLevel(self):
        if self.Step % 100 == 0:
            self.BadGuys.add(DroneShip((640,240)))

    def Run(self):
        
        hmove = 0
        vmove = 0
        
        while self.Playing:
            
            time = clock.tick(60)
            
            self.Step += 1
            self.ProgressLevel()
            self.UpdateAll()
            self.Draw()
            
            self.DetectCollisions()
            
            # Handle Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    
                    if event.key == K_q:
                        self.Playing = False
                        return
                    
                    keystate = pygame.key.get_pressed()
                    
                    if keystate[K_a]==1:
                        hmove = -1
                    elif keystate[K_d]==1:
                        hmove = 1
                    
                    if keystate[K_w]==1:
                        vmove = -1
                    elif keystate[K_s]==1:
                        vmove = 1
                    if keystate[K_j]==1:
                        self.GoodGuy.fire = 1
                        
                elif event.type == pygame.KEYUP:
                    keystate = pygame.key.get_pressed()

                    if keystate[K_a]==0 and hmove<0:
                        hmove = 0
                    if keystate[K_d]==0 and hmove>0:
                        hmove = 0
                    if keystate[K_w]==0:
                        vmove = 0
                    if keystate[K_j]==0:
                        self.GoodGuy.fire = 0
                        
            self.GoodGuy.hmove = hmove
            self.GoodGuy.vmove = vmove
            
            if self.GoodGuy.fire and self.GoodGuy.fired and len(self.GoodBullets)<10 :
                self.AddGoodBullet()
                
            # Refresh Display
            pygame.display.flip()
            
    def AddGoodBullet(self):
        newbullet = GoodBullet(self.GoodGuy.rect.midright)
        self.GoodBullets.add(newbullet)
        
    def DrawScore(self):
        scoretext = self.Font.render("Score : " + str(self.Score) + "   Level : " + str(self.LevelID + 1), 1,(5,225,5))
        self.Surface.blit(scoretext, (400, 447))
        scoretext = self.Font.render("Step : " + str(self.Step), 1,(5,225,5))
        self.Surface.blit(scoretext, (20, 447))
        
    def Draw(self):
        self.Surface.fill((0, 0, 0))
        
        # Draw Level
        self.Level.Draw(self.Step, self.Surface)
        
        # Draw SpriteGroups
        self.PlayerGroup.draw(self.Surface)
        self.GoodBullets.draw(self.Surface)
        self.BadGuys.draw(self.Surface)
        
        for e in self.Explosions:
            e.Draw(self.Surface)
        
        self.Explosions = [e for e in self.Explosions if e.Alive]
        
        # Misc
        self.DrawScore()
            
    def UpdateAll(self):
        self.PlayerGroup.update()
        self.GoodBullets.update()
        self.BadGuys.update()
        for e in self.Explosions:
            e.Update()
            
    def DetectCollisions(self):
        
        contacts = pygame.sprite.groupcollide(self.BadGuys, self.GoodBullets, False, False)
        
        # Good Bullets
        for badguy in contacts.keys():
            
            self.Explosions.append(Explosion(badguy.rect.midleft, badguy.rect.w))
            badguy.kill()
            
            for bullet in contacts[badguy]:
                if bullet: bullet.kill()
