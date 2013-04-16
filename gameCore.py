import pygame
import pygame.sprite
from pygame.locals import *

import random
clock = pygame.time.Clock()

# Libraries
from levelGenerator import Levels
from playerShip import GoodShip, GoodBullet
from droneShip import DroneShip
from droneWing import DroneWing, BadBullet
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
        self.Health = 100
        
        # Bad Guys
        self.BadGuys = pygame.sprite.Group()
        self.BadBullets = pygame.sprite.Group()
        
        # Items
        self.Explosions = []
        
        # Levels
        self.Level = Levels(0)
        self.SetLevel(0)
        
        # Sound
        self.ExpSound = pygame.mixer.Sound("exp.wav")
        
    def SetLevel(self, level):
        self.Step = 0
        self.LevelID = level
        
    def ProgressLevel(self):
        if self.Step % 100 == 0:
            self.BadGuys.add(DroneShip((640,240)))
            self.BadGuys.add(DroneShip((640,140)))
            self.BadGuys.add(DroneWing((640,340)))
            
            self.AddBadBullet((540,340))
            
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
            
            if self.Health<0: self.Playing = False
            
    def AddBadBullet(self, pos):
        b = BadBullet(pos)
        self.BadBullets.add(b)
        
    def AddGoodBullet(self):
        newbullet = GoodBullet(self.GoodGuy.rect.midright)
        self.GoodBullets.add(newbullet)
        
    def DrawScore(self):
        fc = (5,225,5)
        scoretext = self.Font.render("Level : " + str(self.LevelID + 1) + " Score : " + str(self.Score), 1,fc)
        self.Surface.blit(scoretext, (340, 447))
        scoretext = self.Font.render("Step : " + str(self.Step), 1, fc)
        self.Surface.blit(scoretext, (20, 370))
        
        scoretext = self.Font.render("Shields : ", 1, fc)
        self.Surface.blit(scoretext, (20, 445))
        
        x = 130
        y = 450
        
        pygame.draw.rect(self.Surface, Color(255,255,255), Rect(x,y,200,20) , 0)
        
        if self.Health<25:
            hc = Color(255,0,0)
        else:
            hc = Color(255,164,46)
        
        pygame.draw.rect(self.Surface, hc,  Rect(x,y, self.Health*2 ,20) , 0)
        pygame.draw.rect(self.Surface, Color(255,255,255), Rect(x,y,200,20) , 1)
        
    def Draw(self):
        self.Surface.fill((0, 0, 0))
        
        # Draw Level
        self.Level.Draw(self.Step, self.Surface)
        
        # Draw SpriteGroups
        self.PlayerGroup.draw(self.Surface)
        self.GoodBullets.draw(self.Surface)
        self.BadGuys.draw(self.Surface)
        self.BadBullets.draw(self.Surface)
        for e in self.Explosions:
            e.Draw(self.Surface)
        
        self.Explosions = [e for e in self.Explosions if e.Alive]
        
        # Misc
        self.DrawScore()
            
    def UpdateAll(self):
        self.PlayerGroup.update()
        self.GoodBullets.update()
        self.BadBullets.update()
        self.BadGuys.update()
        for e in self.Explosions:
            e.Update()
            
    def DetectCollisions(self):
        
        contacts = pygame.sprite.groupcollide(self.BadGuys, self.GoodBullets, False, False)
        
        # Good Bullets
        for badguy in contacts.keys():
            
            self.Explosions.append(Explosion(badguy.rect.midleft, badguy.rect.w))
            badguy.kill()
            self.ExpSound.play()
            self.Score += badguy.ScoreValue
            for bullet in contacts[badguy]:
                if bullet: bullet.kill()
        
        # Player Bad Guy collision
        contacts = pygame.sprite.spritecollide(self.GoodGuy,self.BadGuys, False)
        
        for badguy in contacts:
            self.Explosions.append(Explosion(badguy.rect.midleft, badguy.rect.w))
            badguy.kill()
            self.ExpSound.play()
            self.Health -= badguy.Damage
