import sys
import pygame
from pygame import *

pygame.init()
window_surface = pygame.display.set_mode((400,500))
pygame.display.set_caption("Hello World")
window_surface.fill((0,0,0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit