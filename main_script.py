import pygame, time, random
from secondary import *
from settings import *
pygame.init()

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25)


# Message to screen
def message_to_screen(x, y, msg, colour=WHITE):
    screen_text = font.render(msg, True, colour)
    screen_text.get_rect()
    GAME_DISPLAY.blit(screen_text, [(WIDTH / 2) - (screen_text.get_rect().width / 2), 0])

cells = [Cell() for x in range(10)]
loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            cells.append(Cell())

    GAME_DISPLAY.fill(WHITE)
    for cell in cells:
        cell.update()

    pygame.display.update()
    clock.tick(FPS)







