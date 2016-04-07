import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 350
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Hello, World!')

screen.fill(WHITE)
pygame.display.update()

pygame.time.wait(4000)

