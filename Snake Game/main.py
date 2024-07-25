import sys
import pygame
from pygame import *
import time
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
SCORES_HEIGHT = WINDOW_HEIGHT - WINDOW_WIDTH
SPACE_SIZE = WINDOW_WIDTH / 20
FPS = 10

class Snake:
    def __init__(self):
        self.x, self.y = SPACE_SIZE, SPACE_SIZE + SCORES_HEIGHT
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, SPACE_SIZE, SPACE_SIZE)
        self.body = [pygame.Rect(self.x-SPACE_SIZE, self.y, SPACE_SIZE, SPACE_SIZE)]
        self.dead = False
        
    def draw(self, screen):
        pygame.draw.rect(screen, "green", self.head)
        for b in self.body:
            pygame.draw.rect(screen, (0,200,0), b)
            
    def update(self):
        
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x = self.body[i+1].x
            self.body[i].y = self.body[i+1].y
        self.head.x += self.xdir * SPACE_SIZE
        self.head.y += self.ydir * SPACE_SIZE
        self.body.remove(self.head)
        
        for part in self.body:
            if self.head.x == part.x and self.head.y == part.y:
                    self.dead = True

class Apple:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH/SPACE_SIZE - 1) * SPACE_SIZE
        self.y = random.randint(0, WINDOW_WIDTH/SPACE_SIZE - 1) * SPACE_SIZE + SCORES_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, SPACE_SIZE, SPACE_SIZE)
        
    def update(self, screen):
        pygame.draw.rect(screen, "red", self.rect)

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont(None, 30)
    
    window_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    scores_surface = pygame.Surface((WINDOW_WIDTH,SCORES_HEIGHT))
    
    scores = 0
    
    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.xdir, snake.ydir = 0, -1
                if event.key == pygame.K_DOWN:
                    snake.xdir, snake.ydir = 0, 1
                if event.key == pygame.K_LEFT:
                    snake.xdir, snake.ydir = -1, 0
                if event.key == pygame.K_RIGHT:
                    snake.xdir, snake.ydir = 1, 0
                    
        window_surface.fill("black")
        
        scores_surface.fill("white")
        window_surface.blit(scores_surface, (0,0))
        
        text_surface = my_font.render("Scores: {}".format(scores), True, "black")
        window_surface.blit(text_surface, ((WINDOW_WIDTH-text_surface.get_width())/2,(SCORES_HEIGHT-text_surface.get_height())/2))
        
        snake.update()
        snake.draw(window_surface)
        
        apple.update(window_surface)
            
        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(snake.head.x, snake.head.y, SPACE_SIZE, SPACE_SIZE))
            apple = Apple()
            scores += 1
        
        if snake.dead or snake.head.x not in range(0, WINDOW_WIDTH) or snake.head.y not in range(SCORES_HEIGHT, WINDOW_HEIGHT):
            pygame.quit()
            sys.exit
            break
        
        pygame.display.update()
        
        clock.tick(FPS)
                
if __name__ == "__main__":
    main()