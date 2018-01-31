# Settings for the game

import pygame; pygame.init()
import random

TITLE = "Game"
WIDTH = 800
HEIGHT = 600
FPS = 60

# Define colors
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


COLOUR_LIST = [WHITE, BLACK, RED, GREEN, BLUE, YELLOW]
RAND_COLOUR = random.choice(COLOUR_LIST)
GAME_DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

