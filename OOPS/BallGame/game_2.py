import pygame, random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((1000,500))
white = 255,255,255
black = 0,0,0

class Ball:

    def __init__(self):
        self.x = random.randint(0, width - 50)
        self.y = random.randint(0, height - 50)
        self.moveX = 1
        self.moveY = 1
        self.radius = 50

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - self.radius:
            self.moveX = -1
        elif self.x < self.radius:
            self.moveX = 1
        elif self.y > height - self.radius:
            self.moveY = -1
        elif self.y < self.radius:
            self.moveY = 1

# ball_1 = Ball()
# ball_2 = Ball()
# ball_3 = Ball()

num = int(input("Enter number of balls : "))
balls = [Ball() for i in range(num)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # pygame.draw.circle(screen, black, [ball_1.x, ball_1.y], ball_1.radius)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, black, [ball_2.x, ball_2.y], ball_2.radius)
    # ball_2.update()
    #
    # pygame.draw.circle(screen, black, [ball_3.x, ball_3.y], ball_3.radius)
    # ball_3.update()

    for i in range(len(balls)):
        pygame.draw.circle(screen, black, [balls[i].x, balls[i].y], balls[i].radius)
        balls[i].update()

    pygame.display.update()