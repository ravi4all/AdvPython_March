import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((1000,500))
white = 255,255,255
black = 0,0,0
x = 0
y = 0
moveX = 1
moveY = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.circle(screen, black, (x,y), 50)
    x += moveX
    y += moveY
    
    if x > width - 50:
        moveX = -1
    elif x < 50:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 50:
        moveY = 1

    pygame.display.update()