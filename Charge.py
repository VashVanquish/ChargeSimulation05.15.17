import pygame, sys
import math
from pygame.locals import *

class Charge():
    def __init__(self, image, charge, mass, newX, newY, screen):
        self.image = image
        self.charge = charge
        self.mass = mass
        self.x = newX
        self.y = newY
        self.xSpeed = 0
        self.ySpeed = 0
        self.window = screen

    def draw(self):
        self.window.blit(self.image, (self.x,self.y))

    def getRadius(self, x, y):
        return pow(((self.x + 12)-(x + 12)),2) + pow(((self.y + 12) - (y + 12)),2)
        
    def accel(self, charge):
        if self.getRadius(charge.getPos()[0],charge.getPos()[1]) > 1225: 
            if self.charge < 0:
                if self.x - charge.getPos()[0] < -20 or self.x - charge.getPos()[0] > 20:                
                    if self.x > charge.getPos()[0]:
                        charge.changeXSpeed(60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
                    elif self.x < charge.getPos()[0]:
                        charge.changeXSpeed(-60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
                if self.y - charge.getPos()[1] < -20 or self.y - charge.getPos()[1] > 20:
                    if self.y > charge.getPos()[1]:
                        charge.changeYSpeed(60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
                    elif self.y < charge.getPos()[1]:
                        charge.changeYSpeed(-60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
            elif self.charge > 0:
                if self.x - charge.getPos()[0] < -20 or self.x - charge.getPos()[0] > 20:
                    if self.x > charge.getPos()[0]:
                        charge.changeXSpeed(-60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
                    elif self.x < charge.getPos()[0]:
                        charge.changeXSpeed(60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
                if self.y - charge.getPos()[1] < -20 or self.y - charge.getPos()[1] > 20:
                    if self.y > charge.getPos()[1]:
                        charge.changeYSpeed(-60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))
                    elif self.y < charge.getPos()[1]:
                        charge.changeYSpeed(60/(self.getRadius(charge.getPos()[0],charge.getPos()[1]) * charge.getMass()))

    def changeXSpeed(self, amnt):
        self.xSpeed += amnt

    def changeYSpeed(self, amnt):
        self.ySpeed += amnt

    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

    def setPos(self, x, y):
        self.x = x
        self.y = y
            
    def collide(self, t):
        myRec = self.getRec()
        wallRec = t
        if(self.rect.x <= wallRec[0]):
            if(self.rect.y <=  wallRec[1]):
                if(((self.rect.x + myRec[2]) >= (wallRec[0]) and ((self.rect.y) + myRec[3] >= (wallRec[1])))):
                    return True
            elif(self.rect.y >= wallRec[1]):
                if(((self.rect.x + myRec[2]) >= (wallRec[0]) and ((self.rect.y) <= (wallRec[1] + wallRec[3])))):
                    return True
        elif(self.rect.x >= wallRec[0]):
            if(self.rect.y >= wallRec[1]):
                if(((self.rect.x) <= (wallRec[0] + wallRec[2])) and ((self.rect.y) <= (wallRec[1] + wallRec[3]))):
                    return True
            elif(self.rect.y <= wallRec[1]):
                if(((self.rect.x) <= (wallRec[0] + wallRec[2])) and ((self.rect.y + myRec[3]) >= (wallRec[1]))):
                    return True
        return False

    def getPos(self):
        return (self.x,self.y)

    def getMass(self):
        return self.mass
                         
    def getRec(self):
        myRec = self.image.get_rect()
        return ( self.x, self.y, myRec[2], myRec[3])
