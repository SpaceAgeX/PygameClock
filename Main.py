import pygame
import math
from datetime import datetime



# pygame setup
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Clock")

Clock = pygame.image.load("Assets/Clock.png").convert()

font1 = pygame.font.SysFont('arial', 72)

class Hand():


    def __init__(self, angle, length, width, color):
        self.angle = angle
        self.length = length
        self.width = width
        self.color = color
    def update(self, angle):
        self.angle = angle

    def draw(self):
        pygame.draw.line(screen, self.color, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2), ((math.cos(self.angle)*self.length)+SCREEN_WIDTH/2, (math.sin(self.angle)*self.length) + SCREEN_HEIGHT/2), self.width)
        pygame.draw.line(screen, self.color, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2), (-(math.cos(self.angle)*self.length/25)+SCREEN_WIDTH/2, -(math.sin(self.angle)*self.length/25) + SCREEN_HEIGHT/2), self.width)



class Date():

    def __init__(self,date):
        self.date = date

    def update(self, date):
        self.date = str(date.month)+"/"+str(date.day)+"/"+str(date.year)

    def draw(self):
        txt = font1.render(self.date, True, (65, 105, 255))
        screen.blit(txt, (600-(txt.get_rect().x/2), 600-(txt.get_rect().y/2)))

def main():
    # On Ready Set Up
    running = True
    clock = pygame.time.Clock()

    angle = 0

    Hour = Hand(-1/2*math.pi,250, 20, (0,0,0))
    Minute = Hand(-1/2*math.pi,400, 10,(0,0,0))
    Second = Hand(-1/2*math.pi,450, 5,(255,0,0))

    DateDisplay = Date(datetime.now())

    #Start the Game Loop

    while running:
        #Set Tick rate
        clock.tick(200)

        #Fill Screen
        screen.fill((0,0,0))
        screen.blit(Clock,(0,0))

        now = datetime.now()
        #print(now.hour+(now.minute/60)+(now.second/3600))
        #int(now.strftime("%H")
        Hour.update(((30*(now.hour+(now.minute/60)+(now.second/3600)-3))/(180/math.pi)))
        Hour.draw()
        Minute.update(((30*(((now.minute+(now.second/60))/5)-3))/(180/math.pi)))
        Minute.draw()
        Second.update(((30*(((now.second+(now.microsecond/1000000))/5)-3))/(180/math.pi)))
        Second.draw()

        DateDisplay.update(now)
        DateDisplay.draw()



        #Check for Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Update Screen
        pygame.display.update()

    pygame.quit()


#Initiate the Game
if __name__ == "__main__":
    main()
