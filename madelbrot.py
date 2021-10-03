import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

max_iterations = 1

def map(x, a, b, A, B) :

    r = b-a
    R = B-A
    X = A + (R/r)*(x-a)
    return X

def mandelbrot (x,y, m) :
    zr = 0
    zi = 0
    count = 0
    mag = pow(x,2) + pow(y, 2)
    for q in range (m) :
        z2r = pow(zr,2) - pow(zi, 2)
        z2i = 2*zr*zi
        zr = z2r + x
        zi = z2i + y
        #print(q)
        #print (zr)
        if (zr>= 1000 or zr <=-1000 ) :
            break
        count = count + 1
    return count

pxarray = pygame.PixelArray(screen)
running = True
x=1

while running : 

    #screen.fill((255,255,255))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    if x <= 40 :
        for i in range (SCREEN_WIDTH) :
            for j in range (SCREEN_HEIGHT) :
                x = map(i, 0, SCREEN_WIDTH, -2.5, 2.5)
                y = map(j, 0, SCREEN_HEIGHT, -2.5, 2.5)
                #print((x,y))
                result = mandelbrot (x,y, max_iterations)
                col = int(map(result, 0, max_iterations, 255, 0))
                pxarray[i][j] = pygame.Color(col,col,col)

    x = x+1
    max_iterations = max_iterations +2

    pygame.display.update()
