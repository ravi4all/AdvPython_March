import pygame
import random

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((1000, 500))
white = 255, 255, 255
black = 0, 0, 0

class Ball:
    def __init__(self):
        self.x = random.randint(0,width-50)
        self.y = random.randint(0,height-50)
        self.moveX = 1
        self.moveY = 1
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -1
        elif self.x < 50:
            self.moveX = 1
        elif self.y > height - 50:
            self.moveY = -1
        elif self.y < 50:
            self.moveY = 1

# ball_1 = Ball()
# ball_2 = Ball()
# ball_3 = Ball()

ballsList = []
for i in range(150):
    ball = Ball()
    ballsList.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # pygame.draw.circle(screen, black, (ball_1.x, ball_1.y), 50)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, black, (ball_2.x, ball_2.y), 50)
    # ball_2.update()
    #
    # pygame.draw.circle(screen, black, (ball_3.x, ball_3.y), 50)
    # ball_3.update()

    for i in range(len(ballsList)):
        pygame.draw.circle(screen, ballsList[i].color, (ballsList[i].x, ballsList[i].y), 50)
        ballsList[i].update()

    pygame.display.update()
