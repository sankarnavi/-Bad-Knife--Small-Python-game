import pygame

import time
import sys
import random
pygame.init()
D_W = 800
D_H = 600
C_W = 73
thing_w = 70
thing_h = 292
a = random.randrange(0, 255)
b = random.randrange(0, 255)
c = random.randrange(0, 255)
color3 = (a, b, c)
color1 = (131, 199, 205)
color2 = (0, 0, 255)
l_red = (200, 0, 0)
l_green = (0, 200, 0)
red = (255, 0, 0)
green = (0, 255, 0)
gameDisplay = pygame.display.set_mode((D_W, D_H))
pygame.display.set_caption('A Bad Knife')
clock = pygame.time.Clock()
carImg = pygame.image.load('apple.png')
KnifeImg = pygame.image.load('knife.png')


def thing_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, color3)
    gameDisplay.blit(text, (20, 50))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, color2)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((D_W / 2), (D_H / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.event.get()

    time.sleep(2)
    pygame.event.clear()
    gameloop()


def button(msg, x, y, w, h, i, a, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, i, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'play':
                gameloop()
            elif action == 'quit':
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(gameDisplay, a, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(15)


def CRASH():
    message_display('You Crashed')


def things(thingx, thingy, thingw, thingh, color):

    gameDisplay.blit(KnifeImg, (thingx, thingy))


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exit")
                sys.exit()
                pygame.quit()
                quit()
        gameDisplay.fill(color1)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A Bad Knife", largeText)
        TextRect.center = ((D_W / 2), (D_H / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO", 150, 450, 100, 50, green, l_green, "play")
        button("Quit", 550, 450, 100, 50, red, l_red, "quit")
        pygame.display.update()
        clock.tick(15)


def gameloop():

    x = (D_W * 0.45)
    y = (D_H * 0.8)
    x_change = 0
    thing_startx = random.randrange(0, D_W)
    thing_starty = -600
    thing_speed = 20
    thing_w = 100
    thing_h = 100
    gameEXit = False
    dodged = 0
    while not gameEXit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEXit = True
                print("exit")
                sys.exit()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(color1)
        things(thing_startx, thing_starty, thing_w, thing_h, color3)
        thing_starty += thing_speed
        car(x, y)
        thing_dodged(dodged)

        if x > D_W - C_W or x < 0:
            CRASH()
        if thing_starty > D_H:
            thing_starty = 0 - thing_h
            thing_startx = random.randrange(0, D_W)
            dodged += 1
        ####
        if y < thing_starty+thing_h:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_w or x+C_W > thing_startx and x + C_W < thing_startx+thing_w:
                print('x crossover')
                CRASH()
        ####
        pygame.display.update()
        clock.tick(120)


game_intro()
gameloop()
sys.exit()
pygame.quit()
quit()
