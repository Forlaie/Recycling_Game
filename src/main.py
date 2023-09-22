import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1280, 700))
gameFinished = False
beginning = True
loading = False
inProgress = False
tutorial = False

listOfFacts = ["The average person has the opportunity to recycle more than 25,000 cans in a lifetime", "About 86% of Canada's plastic waste ends up in landfill, while a meager 9% is recycled", "Making paper from recycled paper reduces the related contribution to air pollution 95%."]
num = random.randint(0, len(listOfFacts)-1)
funFact = listOfFacts[num]

# ocean = pygame.image.load(r'C:\Users\jessi\Downloads\Ocean_background.png')
# park = pygame.image.load(r'C:\Users\jessi\Downloads\Park_background.png')
# city = pygame.image.load(r'C:\Users\jessi\Downloads\city_line.jpg')
# backdropList = [ocean, park, city]
# number = random.randint(0, len(backdropList)-1)
# background = backdropList[number]
background = pygame.image.load(r'../resources/Ocean_background.png')

recyclable1 = pygame.image.load(r'../resources/Recyclables1.png')
recyclable2 = pygame.image.load(r'../resources/Recyclables2.png')
recyclable3 = pygame.image.load(r'../resources/Recyclables3.png')
recyclable4 = pygame.image.load(r'../resources/Recyclables4.png')
recycle = [recyclable1, recyclable2, recyclable3, recyclable4]
type = random.randint(0, len(recycle)-1)

garbage1 = pygame.image.load(r'../resources/Trash1.png')
garbage2 = pygame.image.load(r'../resources/Trash2.png')
garbage3 = pygame.image.load(r'../resources/Trash3.png')
garbage4 = pygame.image.load(r'../resources/Trash4.png')
garbage5 = pygame.image.load(r'../resources/Trash5.png')
garbage6 = pygame.image.load(r'../resources/Trash6.png')
trash = [garbage1, garbage2, garbage3, garbage4, garbage5, garbage6]
kind = random.randint(0, len(trash)-1)

compost1 = pygame.image.load(r'../resources/Compost1.png')
compost2 = pygame.image.load(r'../resources/Compost2.png')
compost3 = pygame.image.load(r'../resources/Compost3.png')
compost4 = pygame.image.load(r'../resources/Compost4.png')
compost5 = pygame.image.load(r'../resources/Compost5.png')
compost = [compost1, compost2, compost3, compost4, compost5]
variety = random.randint(0, len(compost)-1)

electronic1 = pygame.image.load(r'../resources/Electronics1.png')
electronic2 = pygame.image.load(r'../resources/Electronics2.png')
electronic3 = pygame.image.load(r'../resources/Electronics3.png')
electric = [electronic1, electronic2, electronic3]
which = random.randint(0, len(electric)-1)

choose = random.randint(1, 4)

recycleBin = pygame.image.load(r'../resources/Recycle bin.png')
garbageCan = pygame.image.load(r'../resources/Trash bin.png')
compostBin = pygame.image.load(r'../resources/Compost_bin.png')
electricBox = pygame.image.load(r'../resources/Electronic_bin.png')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
myFont = pygame.font.SysFont("Times New Roman", 30)
clock = pygame.time.Clock()
start = myFont.render("Start?", 1, black)
fact = myFont.render(funFact, 1, black)
load = myFont.render("Loading...", 1, black)
learn = myFont.render("Tutorial?", 1, black)
wrong = 0
strikes = myFont.render(str(wrong) + " X", 1, black)
garbage_x = random.randint(0, 1205)
garbage_y = -125

while gameFinished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameFinished = True

    keys = pygame.key.get_pressed()

    if keys[ord('p')]:
        gameFinished = True

    mousecor = pygame.mouse.get_pos()
    mouseXcor = mousecor[0]
    mouseYcor = mousecor[1]

    if beginning == True:
        screen.blit(background, (0, 0))
        screen.blit(start, [400, 300])
        screen.blit(learn, [700, 300])
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 400 < mouseXcor < 465 and 300 < mouseYcor < 330:
            loading = True
            beginning = False
        if event.type == pygame.MOUSEBUTTONDOWN and 700 < mouseXcor < 810 and 300 < mouseYcor < 330:
            tutorial = True
            beginning = False

    if tutorial == True:
        screen.blit(background, (0, 0))
        pygame.display.update()
        welcome = myFont.render("Welcome to this recycling game!", 1, black)
        screen.blit(welcome, [450, 50])
        intro = myFont.render("Items will fall out of the sky and you will need to sort them properly!", 1, black)
        screen.blit(intro, [200, 150])
        q = myFont.render("Hold Q for the garbage can, and then click on the item", 1, black)
        screen.blit(q, [300, 250])
        r = myFont.render("Hold R for the recycling bin, and then click on the item", 1, black)
        screen.blit(r, [300, 350])
        w = myFont.render("Hold W for the compost bin, and then click on the item", 1, black)
        screen.blit(w, [300, 450])
        e = myFont.render("Hold E for the electrical box, and then click on the item", 1, black)
        screen.blit(e, [300, 550])
        exit = myFont.render("Press P at anytime to quit", 1, black)
        screen.blit(exit, [450, 650])
        pygame.display.update()
        # screen.blit(background, (0, 0))
        # begin = myFont.render("Press S to start", 1, black)
        # screen.blit(begin, [450, 350])
        # pygame.display.update()
        # if keys[ord('s')]:
        #     loading = True
        #     tutorial = False

    if loading == True:
        screen.blit(background, (0, 0))
        screen.blit(load, [500, 300])
        screen.blit(fact, [100, 450])
        screen.blit(strikes, [50, 50])
        pygame.display.update()
        screen.blit(background, (0, 0))
        screen.blit(load, [500, 300])
        screen.blit(fact, [100, 450])
        screen.blit(strikes, [50, 50])
        countdown = myFont.render("3", 1, black)
        screen.blit(countdown, [700, 300])
        pygame.display.update()
        time.sleep(1)
        screen.blit(background, (0, 0))
        screen.blit(load, [500, 300])
        screen.blit(fact, [100, 450])
        screen.blit(strikes, [50, 50])
        countdown = myFont.render("2", 1, black)
        screen.blit(countdown, [700, 300])
        pygame.display.update()
        time.sleep(1)
        screen.blit(background, (0, 0))
        screen.blit(load, [500, 300])
        screen.blit(fact, [100, 450])
        screen.blit(strikes, [50, 50])
        countdown = myFont.render("1", 1, black)
        screen.blit(countdown, [700, 300])
        pygame.display.update()
        time.sleep(1)
        screen.blit(background, (0, 0))
        screen.blit(load, [500, 300])
        screen.blit(fact, [100, 450])
        screen.blit(strikes, [50, 50])
        countdown = myFont.render("Go!", 1, black)
        screen.blit(countdown, [700, 300])
        pygame.display.update()
        inProgress = True
        loading = False

    if inProgress == True:
        if garbage_y >= -125 and garbage_y <= 700:
            screen.blit(background, (0, 0))
            if choose == 1:
                screen.blit(trash[kind], (garbage_x, garbage_y))
            elif choose == 2:
                screen.blit(recycle[type], (garbage_x, garbage_y))
            elif choose == 3:
                screen.blit(compost[variety], (garbage_x, garbage_y))
            elif choose == 4:
                screen.blit(electric[which], (garbage_x, garbage_y))
            screen.blit(strikes, [50, 50])
            pygame.display.update()
            garbage_y += 3
        if garbage_y >= 700:
            choose = random.randint(1, 4)
            if choose == 1:
                kind = random.randint(0, len(trash) - 1)
            elif choose == 2:
                type = random.randint(0, len(recycle)-1)
            elif choose == 3:
                variety = random.randint(0, len(compost)-1)
            elif choose == 4:
                which = random.randint(0, len(electric)-1)
            garbage_x = random.randint(100, 1000)
            garbage_y = -125
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, black)

        if keys[ord('q')]:
            screen.blit(garbageCan, (540, 480))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose == 1:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
            elif event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose != 1:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
                wrong += 1
                strikes = myFont.render(str(wrong) + " X", 1, black)

        elif keys[ord('r')]:
            screen.blit(recycleBin, (550, 430))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose == 2:
                #choose = random.randint(1, 3)
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
            elif event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose != 2:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
                wrong += 1
                strikes = myFont.render(str(wrong) + " X", 1, black)

        elif keys[ord('w')]:
            screen.blit(compostBin, (550, 400))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose == 3:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
            elif event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose != 3:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
                wrong += 1
                strikes = myFont.render(str(wrong) + " X", 1, black)

        elif keys[ord('e')]:
            screen.blit(electricBox, (540, 480))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose == 4:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
            elif event.type == pygame.MOUSEBUTTONDOWN and garbage_x <= mouseXcor <= garbage_x + 225 and garbage_y <= mouseYcor <= garbage_y + 225 and choose != 4:
                choose = random.randint(1, 4)
                if choose == 1:
                    kind = random.randint(0, len(trash) - 1)
                elif choose == 2:
                    type = random.randint(0, len(recycle) - 1)
                elif choose == 3:
                    variety = random.randint(0, len(compost) - 1)
                elif choose == 4:
                    which = random.randint(0, len(electric) - 1)
                garbage_x = random.randint(100, 1000)
                garbage_y = -125
                wrong += 1
                strikes = myFont.render(str(wrong) + " X", 1, black)

pygame.quit()
quit()