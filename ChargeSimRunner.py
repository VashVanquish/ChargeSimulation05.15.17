import pygame, sys
from pygame.locals import *
from Charge import *
from Cursor import *
from Statics import *
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Charge Simulation by Mason Lanham")
pygame.display.set_icon(pygame.image.load("PlusML.png"))
pygame.key.set_repeat(300,300)
pygame.mouse.set_visible(False)
cursor = Cursor(0,0,screen)
keyCursor = KeyCursor(screen)
statics = Statics(screen)
staticCharges = (StaticPlus(screen),StaticMinus(screen))
buttons = (StartButton(screen), ClearButton(screen))
m = pygame.image.load("plusM.png")
mode = 0
SelecCharge = 0
cOS = []
while True:
    # Interface Controls ETC.
    while mode == 0:
        screen.fill((0,0,0))
        plusM = Charge(m, 1, keyCursor.getMass(), 500, 280, screen)
        cursor.setPos(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    keyCursor.moveDown()
                elif event.key == K_RIGHT:
                    keyCursor.moveRight()
                elif event.key == K_LEFT:
                    keyCursor.moveLeft()
                elif event.key == K_UP:
                    keyCursor.moveUp()
            
            elif event.type==MOUSEBUTTONDOWN:
                if SelecCharge == 0:
                    for x in staticCharges:
                        if cursor.collide(x.getRec()):
                            cursor.changeImage()
                            if x.ToF():
                                SelecCharge = Charge(pygame.image.load("Plus.png"), 1, keyCursor.getMass(), cursor.getPos()[0], cursor.getPos()[1], screen)
                            else:
                                SelecCharge = Charge(pygame.image.load("Minus.png"), -1, keyCursor.getMass(), cursor.getPos()[0], cursor.getPos()[1], screen)
                    for x in cOS:
                        if cursor.collide(x.getRec()):
                            cursor.changeImage()
                            SelecCharge = x
                else:
                    cursor.changeImage()
                    cOS.append(SelecCharge)
                    SelecCharge = 0
                for x in buttons:
                    if cursor.collide(x.getRec()):
                        mode = x.getMode()
                    
        statics.draw()
        if len(cOS) > 0:
            for x in cOS:
                if x.getPos()[0] >= 800:
                    cOS.remove(x)
                x.draw()
        for x in staticCharges:
            x.draw()
        for x in buttons:
            x.draw()
        keyCursor.draw()
        plusM.draw()
        if SelecCharge != 0:
            SelecCharge.setPos(cursor.getPos()[0] + 6,cursor.getPos()[1] + 6)
            SelecCharge.draw()
        cursor.draw()
        """for x in pOS:
            x.draw()
            if x.getState() >= 18:
                if cursor.collide(x.getRec()):"""
        pygame.display.update()
        pygame.time.delay(10)
    while mode == 2:
        for x in cOS:
            cOS.remove(x)
            for x in cOS:
                cOS.remove(x)
        for x in cOS:
            cOS.remove(x)
            for x in cOS:
                cOS.remove(x)
            
        mode = 0

    while mode == 1:
        #Actual Simulation Code
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mode = 0
                elif event.key == K_RIGHT:
                    mode = 0
                elif event.key == K_LEFT:
                    mode = 0
                elif event.key == K_UP:
                    mode = 0
        for x in cOS:
            x.draw()
            x.accel(plusM)
        plusM.move()
        plusM.draw()
        pygame.display.update()
        pygame.time.delay(1)
                    
            



