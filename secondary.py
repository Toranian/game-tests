import pygame, time, random
from settings import *
pygame.init()


class Cell:

    def __init__(self):
        self.speed = random.randint(1, 4)
        self.colour = RAND_COLOUR
        self.size = random.randint(5, 20)
        self.loc_x = random.randint(0, WIDTH)
        self.loc_y = random.randint(0, HEIGHT)
        self.dir_x = random.randint(-self.speed, self.speed)
        self.dir_y = random.randint(-self.speed, self.speed)

    def update(self):

        if self.loc_x >= WIDTH - self.size:
            self.dir_x = -self.speed

        elif self.loc_x <= 0 + self.size:
            self.dir_x = self.speed

        elif self.loc_y >= HEIGHT - self.size:
            self.dir_y = -self.speed

        elif self.loc_y <= 0 + self.size:
            self.dir_y = self.speed

        self.loc_x += self.dir_x
        self.loc_y += self.dir_y
        pygame.draw.circle(GAME_DISPLAY, self.colour, [self.loc_x, self.loc_y], self.size)






