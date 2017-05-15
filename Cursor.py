import pygame
from pygame.locals import *
class Cursor(pygame.sprite.Sprite):
    def __init__(self, newX, newY, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Cursor0.png")
        self.images = (pygame.image.load("Cursor0.png"),pygame.image.load("Cursor1.png"))
        self.rect = self.image.get_rect()
        self.rect.x = newX
        self.rect.y = newY
        self.i = 0
        self.window = screen
        
    def draw(self):
        self.window.blit(self.image, (self.rect[0], self.rect[1]))

    def setPos(self, pos):
        self.rect.x = pos[0] - (self.rect[2]/2)
        self.rect.y = pos[1] - (self.rect[3]/2)

    def changeImage(self):
        if self.i == 0:
            self.i = 1
        else:
            self.i = 0
        self.image = self.images[self.i]
        
    def moveLeft(self):
        self.rect[0] = self.rect[0] - self.rate        
        if self.rect[0] < 0:
            self.rect[0] = self.rect[0] + self.rate
            
    def moveUpLeft(self):
        self.rect[0] = self.rect[0] - self.rate
        self.rect[1] = self.rect[1] - self.rate
        if self.rect[0] < 0:
            self.rect[0] = self.rect[0] + self.rate
        if self.rect[1] < 0:
            self.rect[1] = self.rect[1] + self.rate
            
    def moveDownLeft(self):
        self.rect[0] = self.rect[0] - self.rate
        self.rect[1] = self.rect[1] + self.rate
        if self.rect[0] < 0:
            self.rect[0] = self.rect[0] + self.rate
        if self.rect[1] + self.rect[3] > 600:
            self.rect[1] = self.rect[1] - self.rate
            
    def moveRight(self):
        self.rect[0] = self.rect[0] + self.rate
        if self.rect[0] + self.rect[2] > 800:
            self.rect[0] = self.rect[0] - self.rate            

    def moveUpRight(self):
        self.rect[0] = self.rect[0] + self.rate
        self.rect[1] = self.rect[1] - self.rate
        if self.rect[0] + self.rect[2] > 800:
            self.rect[0] = self.rect[0] - self.rate
        if self.rect[1] < 0:
            self.rect[1] = self.rect[1] + self.rate
            
    def moveDownRight(self):
        self.rect[0] = self.rect[0] + self.rate
        self.rect[1] = self.rect[1] + self.rate
        if self.rect[0] + self.rect[2] > 800:
            self.rect[0] = self.rect[0] - self.rate
        if self.rect[1] + self.rect[3] > 600:
            self.rect[1] = self.rect[1] - self.rate
            
    def moveUp(self):
        self.rect[1] = self.rect[1] - self.rate
        if self.rect[1] < 0:
            self.rect[1] = self.rect[1] + self.rate
        
    def moveDown(self):
        self.rect[1] = self.rect[1] + self.rate
        myRec = self.getRec()
        if self.rect[1] + myRec[3] > 600:
            self.rect[1] = self.rect[1] - self.rate

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
        return (self.rect[0],self.rect[1])
    
    def getRec(self):
        myRec = self.image.get_rect()
        return (self.rect[0], self.rect[1], myRec[2], myRec[3])

class KeyCursor():
    def __init__(self, screen):
        self.image = pygame.image.load("KeyCursor.png")
        self.x = 803
        self.y = 140
        self.row = 0
        self.col = 0
        self.screen = screen
        self.massMatrix = ((1, 2, 5),
                           (10,20,30),
                           (40,50,60),
                           (70,80,90))

    def moveRight(self):
        if self.row != 4:
            if self.col < len(self.massMatrix[self.row]) - 1:
                self.col += 1
                self.x += 60
            else:
                self.col = 0
                self.x = 803
    def moveLeft(self):
        if self.row != 4:
            if self.col != 0:
                self.col -= 1
                self.x -= 60
            else:
                self.col = 2
                self.x = 923
        if self.x < 803:
            self.x = 803
    def moveDown(self):
        self.col == 0
        self.x = 803
        if self.row < len(self.massMatrix) - 1:
            self.row += 1
            self.y += 48
        else:
            self.row = 0
            self.y = 140
    def moveUp(self):
        self.col == 0
        self.x = 803
        if self.row != 0:
            self.row -= 1
            self.y -= 48
        else:
            self.row = 3
            self.y = 284

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def getMass(self):
        return self.massMatrix[self.row][self.col]

