import pygame
import pygame.sprite
from pygame.locals import *

# Libraries
import os
import random
clock = pygame.time.Clock()

# Daft
from levelGenerator import Levels
from playerShip import GoodShip, GoodBullet
from droneShip import DroneShip
from droneWing import DroneWing, BadBullet
from droneTower import DroneTower
from droneSnakehead import DroneSnakeHead
from animExplosion import Explosion
from niceThings import ShieldBoost


def LoadImg(filename):
    return pygame.image.load(os.path.join("img", filename))

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
        self.Bonuses = pygame.sprite.Group()
        
        # Levels
        self.Level = Levels(0)
        self.SetLevel(0)
        
        # Sound
        self.ExpSound = pygame.mixer.Sound("exp.wav")
        self.BonusSound = pygame.mixer.Sound("bonus.wav")
        self.HurtSound = pygame.mixer.Sound("hurt.wav")
        
        self.LoadGFX()
        
    def LoadGFX(self):
        self.ShieldBoostImgs = [LoadImg("shieldb0.png"),
                                LoadImg("shieldb1.png"),
                                LoadImg("shieldb2.png"),
                                LoadImg("shieldb3.png"),
                                LoadImg("shieldb3.png"),
                                LoadImg("shieldb2.png"),
                                LoadImg("shieldb1.png")]
        self.DroneShipImgs = [LoadImg("drone1.png"),
                         LoadImg("drone2.png"),
                         LoadImg("drone3.png")]
        self.DroneWingImgs = [LoadImg("shortwing1.png")]
        
        self.BadBulletImgs = [LoadImg("badbullet.png")]
        self.GoodBulletImgs = [LoadImg("bullet.png")]
        self.TowerImgs = [LoadImg("tower0.png"), LoadImg("tower1.png"), LoadImg("tower2.png") ]
        
        self.SnakeheadImgs = [LoadImg("snake0.png")]
        
    def SetLevel(self, level):
        self.Step = 0
        self.LevelID = level
        
    def ProgressLevel(self):
        """
            Keep things changing.
        """
        if self.Step % 100 == 0  and self.Step<300:
            self.BadGuys.add( DroneShip((640,240), self.DroneShipImgs) )
            self.BadGuys.add( DroneShip((640,140), self.DroneShipImgs) )
            
        elif self.Step>300  and self.Step<900  and self.Step % 100 == 0:
            
            dw = DroneWing((640,40), self.DroneWingImgs)
            self.BadGuys.add( dw )
            dw.gameCore = self
            dw.targetvert = self.GoodGuy.rect.midright[0]
            
            dw = DroneWing((640,400), self.DroneWingImgs)
            self.BadGuys.add( dw )
            dw.targetvert = self.GoodGuy.rect.midright[0]
            dw.gameCore = self
            
        elif self.Step>900  and self.Step<1200  and self.Step % 70 == 0:
            sh = DroneSnakeHead((640,40), self.SnakeheadImgs)
            self.BadGuys.add(sh)
            sh.gameCore = self
            
        elif self.Step>1200  and self.Step<1800  and self.Step % 40 == 0:
            dt = DroneTower((640,344), self.TowerImgs)
            self.BadGuys.add( dt )
            dt.gameCore = self
    
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
        b = BadBullet(pos, self.BadBulletImgs)
        self.BadBullets.add(b)
        return b
        
    def AddGoodBullet(self):
        newbullet = GoodBullet(self.GoodGuy.rect.midright, self.GoodBulletImgs)
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
        #self.Surface.fill((0, 0, 0))
        
        # Draw Level
        self.Level.Draw(self.Step, self.Surface)
        
        # Draw SpriteGroups
        self.PlayerGroup.draw(self.Surface)
        self.Bonuses.draw(self.Surface)
        self.BadGuys.draw(self.Surface)
        
        for e in self.Explosions:
            e.Draw(self.Surface)
        self.GoodBullets.draw(self.Surface)
        self.BadBullets.draw(self.Surface)
        
        # Tidy up explosions
        self.Explosions = [e for e in self.Explosions if e.Alive]
        
        # Misc
        self.DrawScore()
            
    def UpdateAll(self):
        self.PlayerGroup.update()
        self.GoodBullets.update()
        self.BadBullets.update()
        self.BadGuys.update()
        self.Bonuses.update()
        for e in self.Explosions:
            e.Update()
            
    def DetectCollisions(self):
        
        # Good Bullets
        contacts = pygame.sprite.groupcollide(self.BadGuys, self.GoodBullets, False, False)
        
        for badguy in contacts.keys():
            
            badguy.HitsToDie -= 1
            
            if badguy.HitsToDie < 1:
                self.Explosions.append(Explosion(badguy.rect.midleft, badguy.rect.w))
                badguy.kill()
                self.ExpSound.play()
                self.Score += badguy.ScoreValue
                
                if random.randrange(0,5) == 3:
                    sb = ShieldBoost(badguy.rect.center, self.ShieldBoostImgs)
                    self.Bonuses.add(sb)

            for bullet in contacts[badguy]:
                if bullet: bullet.kill()
        
        # Bad Bullets
        contacts = pygame.sprite.spritecollide(self.GoodGuy, self.BadBullets, False)
        
        for badbullet in contacts:
            badbullet.kill()
            self.HurtSound.play()
            self.Health -= 10
        
        # Player Bad Guy collision
        contacts = pygame.sprite.spritecollide(self.GoodGuy, self.BadGuys, False)
        
        for badguy in contacts:
            self.Explosions.append(Explosion(badguy.rect.midleft, badguy.rect.w))
            badguy.kill()
            self.ExpSound.play()
            self.Health -= badguy.Damage

        # Player Bonus Collect
        contacts = pygame.sprite.spritecollide(self.GoodGuy, self.Bonuses, False)
        
        for bonus in contacts:
            bonus.kill()
            self.BonusSound.play()
            self.Health += bonus.Health
            if self.Health>100: self.Health = 100
