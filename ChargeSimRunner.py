import pygame, sys
from pygame.locals import *
from Charge import *
from Cursor import *
from Statics import *
pygame.init()
screen = pygame.display.set_mode((1000,600))#Sets the Size of the Window
pygame.display.set_caption("Charge Simulation by Mason Lanham") #Changes the Name of the Window
pygame.display.set_icon(pygame.image.load("PlusML.png")) #Changes the Icon in top left
pygame.key.set_repeat(300,300) #Sets the interval at which button presses are detected 
pygame.mouse.set_visible(False) #Turns the Standard cursor invisible
cursor = Cursor(0,0,screen) #Initialize my cursor object
keyCursor = KeyCursor(screen) #Initializes the cursor controled by the keys
statics = Statics(screen) #Initializes the static images as an object
staticCharges = (StaticPlus(screen),StaticMinus(screen)) #Initializes the Charges that you can drag
buttons = (StartButton(screen), ClearButton(screen)) #Initializes the on screen buttons
m = pygame.image.load("plusM.png") #loads the image that will be used to initalize the green charge
mode = 0 #integer variable that is used to change between while loops
SelecCharge = 0 # this reference will be used later
cOS = [] # list that will contain all charge objects on screen
while True:
    # Interface Controls ETC.
    while mode == 0:
        screen.fill((0,0,0))
        plusM = Charge(m, 1, keyCursor.getMass(), 500, 280, screen) #Initializes new plusM object
        #The reason I create a new one is so that it has the right mass
        cursor.setPos(pygame.mouse.get_pos()) # keeps track of where the OS cursor is and sets my cursor position to that
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
        pygame.display.update()
        pygame.time.delay(10)

    while mode == 2:
        #Not Sure Why, but I had to remove everything this many times to get it to actually remove all of the items in this list
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
        #Actual Simulation Code Occurs when you hit start button
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                #I didn't feel like writing out "or" so many times here
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
            x.accel(plusM) # accelerates the charge object that you pass it
        plusM.move()
        plusM.draw()
        pygame.display.update()
        pygame.time.delay(1) # I delay slightly so that it doesn't get too crazy
