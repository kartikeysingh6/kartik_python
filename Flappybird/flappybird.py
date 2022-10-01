import pygame
import random
import time
import os

start1 = 0
stop1 = 0
stop2 = 0
pygame.init()
screen = pygame.display.set_mode((600, 500))

done = False
y = 200
e = 0
h = 0
r = 0
j = 0
a = 0
s = 0
w = 0
score = 0
l = [0]
v = [600]

start1 = time.time()
img1 = pygame.image.load(os.path.join(
    os.path.dirname(__file__), '.', 'flappybird2.png'))
cloud1 = pygame.image.load(os.path.join(
    os.path.dirname(__file__), '.', 'cloud1.png'))
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('comicsancms', 65)
text1 = font1.render('GAME OVER', True, (10, 10, 10))
font3 = pygame.font.SysFont('comicsancms', 30)
text4 = font3.render('Press RETURN To Exit', True, (10, 10, 10))
font2 = pygame.font.SysFont('comicsancms', 50)
sound1 = pygame.mixer.Sound(os.path.join(
    os.path.dirname(__file__), '.', './sfx_point.wav'))
sound2 = pygame.mixer.Sound(os.path.join(
    os.path.dirname(__file__), '.', './sfx_hit.wav'))
sound3 = pygame.mixer.Sound(os.path.join(
    os.path.dirname(__file__), '.', './sfx_wing.wav'))

while not done:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True

    clock.tick(120)

    screen.fill((255, 255, 255))
    screen.blit(cloud1, (-100, 5))
    screen.blit(cloud1, (280, 20))
    screen.blit(cloud1, (500, 10))
    screen.blit(img1, (200, y))

    press = pygame.key.get_pressed()
    stop2 = time.time()
    text3 = font1.render('%d' % (4-(stop2-start1)), True, (0, 0, 0))

    if e == 0:
        screen.blit(text3, (300-text3.get_width() //
                    2, 250-text3.get_height()//2))
        pygame.display.flip()

    if (stop2-start1) >= 4:
        e = 1

    if w == 1 and press[pygame.K_RETURN]:
        done = True

    if w == 0 and e == 1:

        stop1 = time.time()

        for k in range(a):
            v[k] -= 1.5

        if (stop1-start1) >= 1.5:
            l[a] = random.randrange(-320, 0)
            l.append(0)
            v.append(600)
            a += 1
            if a > 9:
                v.remove(v[0])
                l.remove(l[0])
                a = 9
            start1 = time.time()
            j += 1
            if j > 9:
                j = 0

        if press[pygame.K_SPACE]:
            sound3.stop()
            sound3.play(0)
            r = 1

        if r == 1:
            h = 2.8
            r = 2

        if r == 2:
            y = y-h
            h -= 0.2
            if h <= 0:
                r = 0

        if r == 0 and y < 475:
            y = y+h
            h += 0.1

        for k in range(a):
            pygame.draw.rect(screen, (10, 200, 10),
                             pygame.Rect(v[k], l[k], 60, 400))
            pygame.draw.rect(screen, (10, 200, 10),
                             pygame.Rect(v[k], 490+l[k], 60, 400))
            pygame.draw.rect(screen, (10, 220, 10),
                             pygame.Rect(v[k]-2, 370+l[k], 64, 30))
            pygame.draw.rect(screen, (10, 220, 10),
                             pygame.Rect(v[k]-2, 490+l[k], 64, 30))

        if y >= 475:
            y = 475
            w = 1
            sound3.stop()
            sound2.play(0)
            screen.blit(text1, (300-text1.get_width() //
                        2, 250-text1.get_height()//2))
            screen.blit(text4, (300-text4.get_width()//2, 280))

        if y <= 0:
            y = 0
            w = 1
            sound3.stop()
            sound2.play(0)
            screen.blit(text1, (300-text1.get_width() //
                        2, 250-text1.get_height()//2))
            screen.blit(text4, (300-text4.get_width()//2, 280))

        for s in range(a):

            if v[s] <= 236 and v[s] >= 140:
                if y <= (l[s]+400)-4 or y >= (l[s]+490)-24:
                    screen.blit(text1, (300-text1.get_width() //
                                2, 250-text1.get_height()//2))
                    screen.blit(text4, (300-text4.get_width()//2, 280))
                    w = 1
                    sound3.stop()
                    sound2.play(0)
                    break

                elif v[s] >= 199.5 and v[s] <= 200.5:
                    score += 1
                    sound3.stop()
                    sound1.play(0)

        text2 = font2.render('SCORE: {}'.format(score), True, (10, 10, 10))

        screen.blit(text2, (430, 20))
        pygame.display.flip()

print('Your score: {}'.format(score))
