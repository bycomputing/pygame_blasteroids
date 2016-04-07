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

rock_plot_points = [(5,0), (0,15), (0,30),
                    (15,40), (20,30), (30,40),
                    (45,30), (45,25), (25,20),
                    (45,10), (36,0), (25,5)]

rock_surf = pygame.Surface((51, 41))
rock_draw_position = 10, 10

pygame.draw.polygon(rock_surf, WHITE, rock_plot_points, 1)

screen.blit(ship_surf, position)
screen.blit(rock_surf, rock_draw_position)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()



