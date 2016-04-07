import pygame
import sys
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 350
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('My Awesome Game')

ship_surf = pygame.Surface((17, 21))
position = 100, 100

pygame.draw.line(ship_surf, GREEN, [0, 20], [8, 0])
pygame.draw.line(ship_surf, GREEN, [8, 0], [16, 20])
pygame.draw.line(ship_surf, GREEN, [2, 15], [7, 15])
pygame.draw.line(ship_surf, GREEN, [14, 15], [9, 15])

screen.blit(ship_surf, position)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()



