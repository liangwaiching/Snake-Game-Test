import sys
import pygame
from pygame import *
import time

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
SCORES_HEIGHT = WINDOW_HEIGHT-WINDOW_WIDTH
BACKGROUND_COLOR = (0,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    window_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    scores_surface = Surface((WINDOW_WIDTH,SCORES_HEIGHT))
    scores = 0
    my_font = pygame.font.SysFont(None, 30)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
                
        window_surface.fill(BACKGROUND_COLOR)
        scores_surface.fill(WHITE)
        
        text_surface = my_font.render("Scores: {}".format(scores), True, BLACK)
        window_surface.blit(scores_surface, (0,0))
        window_surface.blit(text_surface, ((WINDOW_WIDTH-text_surface.get_width())/2,(SCORES_HEIGHT-text_surface.get_height())/2))
        
        pygame.display.update()
        clock.tick(FPS)
                
if __name__ == "__main__":
    main()