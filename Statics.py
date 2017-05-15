import pygame
from pygame.locals import *

class Statics():
    def __init__(self, screen):
        self.panel = pygame.image.load("RightPanel.png")
        self.massPanel = pygame.image.load("MassPanel.png")
        self.screen = screen
        
    def draw(self):
        self.screen.blit(self.panel,(800,0))
        self.screen.blit(self.massPanel,(800,90))
        
class StaticPlus(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Plus.png")
        self.rect = self.image.get_rect()
        self.rect.x = 888
        self.rect.y = 20
        self.window = screen
        
    def draw(self):
        self.window.blit(self.image, (self.rect[0], self.rect[1]))

    def ToF(self):
        return True

    def getPos(self):
        return (self.rect[0],self.rect[1])
    
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.rect[0], self.rect[1], myRec[2], myRec[3])
    
class StaticMinus(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Minus.png")
        self.rect = self.image.get_rect()
        self.rect.x = 888
        self.rect.y = 60
        self.window = screen
        
    def draw(self):
        self.window.blit(self.image, (self.rect[0], self.rect[1]))

    def ToF(self):
        return False

    def getPos(self):
        return (self.rect[0],self.rect[1])
    
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.rect[0], self.rect[1], myRec[2], myRec[3])

class StartButton(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Start.png")
        self.rect = self.image.get_rect()
        self.rect.x = 855
        self.rect.y = 360
        self.window = screen

    def draw(self):
        self.window.blit(self.image, (self.rect[0], self.rect[1]))

    def getPos(self):
        return (self.rect[0],self.rect[1])
    
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.rect[0], self.rect[1], myRec[2], myRec[3])

    def getMode(self):
        return 1

class ResetButton(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Reset.png")
        self.rect = self.image.get_rect()
        self.rect.x = 844
        self.rect.y = 470
        self.window = screen

    def draw(self):
        self.window.blit(self.image, (self.rect[0], self.rect[1]))

    def getPos(self):
        return (self.rect[0],self.rect[1])
    
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.rect[0], self.rect[1], myRec[2], myRec[3])

    def getMode(self):
        return 0

class ClearButton(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Clear.png")
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = 460
        self.window = screen

    def draw(self):
        self.window.blit(self.image, (self.rect[0], self.rect[1]))

    def getPos(self):
        return (self.rect[0],self.rect[1])
    
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.rect[0], self.rect[1], myRec[2], myRec[3])

    def getMode(self):
        return 2

    





