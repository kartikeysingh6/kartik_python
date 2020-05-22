import math
import random

import pygame
from pygame import mixer
print("\n\nGame created by Heisenberg\n------------------------------------------------------\nCONTROLS:\nUse A for Left, D for Right and SPACEBAR to fire gun.\n------------------------------------------------------\nDISCLAIMER:\nThis game is strictly for entertainment purpose only.\n------------------------------------------------------")
try:
    noes = int(input("Enter No. of enemies:(6 is default) "))
    while(noes<=0 or noes>50):
        print("Allowed Range is only [1,50]")
        noes = int(input("Enter No. of enemies: "))
except:
    noes=6

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('manit.png')
mixer.music.load("bella.mp3")
mixer.music.play(-1)
pygame.display.set_caption("Kill NSR")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#gun model
playerImg = pygame.image.load('bandook.png')
playerX = 370
playerY = 480
playerX_change = 0

#Dushman
dushmanImg = []
dushmanX = []
dushmanY = []
dushmanX_change = []
dushmanY_change = []
num_of_enemies = noes

for i in range(num_of_enemies):
    dushmanImg.append(pygame.image.load('dushman.png'))
    dushmanX.append(random.randint(0, 736))
    dushmanY.append(random.randint(50, 150))
    dushmanX_change.append(4)
    dushmanY_change.append(40)

# Ready: bullet is hidden
# Fire: bullet is projectile

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

#MANIT DESTORYED aka Game Over!
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("NSR Killed : " + str(score_value), True, (255, 165, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text1 = over_font.render("Game Over!", True, (255, 0, 255))
    over_text2 = over_font.render("MANIT Destoryed!", True, (255, 0, 0))
    screen.blit(over_text1, (210, 220))
    screen.blit(over_text2, (140, 350))


def player(x, y):
    screen.blit(playerImg, (x, y))


def dushman(x, y, i):
    screen.blit(dushmanImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(dushmanX, dushmanY, bulletX, bulletY):
    distance = math.sqrt(math.pow(dushmanX - bulletX, 2) + (math.pow(dushmanY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


#game in the loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                score_value+=10
                print("Score toh badha lia pr tu cheater hai saale")
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("gunshot.wav")
                    bulletSound.play()
                    #getsXcordinate
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #dushman ki gatividhi
    for i in range(num_of_enemies):

        #ENd of game aka over
        if dushmanY[i] > 440:
            for j in range(num_of_enemies):
                dushmanY[j] = 2000
            game_over_text()
            break

        dushmanX[i] += dushmanX_change[i]
        if dushmanX[i] <= 0:
            dushmanX_change[i] = 4
            dushmanY[i] += dushmanY_change[i]
        elif dushmanX[i] >= 736:
            dushmanX_change[i] = -4
            dushmanY[i] += dushmanY_change[i]

        #collison
        collision = isCollision(dushmanX[i], dushmanY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("death.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            dushmanX[i] = random.randint(0, 736)
            dushmanY[i] = random.randint(50, 150)

        dushman(dushmanX[i], dushmanY[i], i)

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
