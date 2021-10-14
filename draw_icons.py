import pygame
import math
# 靛青色(8,46,84)
screen = pygame.display.set_mode((800,600))
pygame.init()

def draw():
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (115, 15), 15, 1)
    pygame.draw.circle(screen, (0, 0, 0), (115, 44), 15, 1)
    pygame.draw.rect(screen, (0, 0, 0), (108, 8, 14, 14), 1)
    pygame.draw.line(screen, (0, 0, 0), (108, 37), (122, 51), 3)
    pygame.draw.line(screen, (0, 0, 0), (108, 51), (122, 37), 3)
    pygame.draw.line(screen, (0, 0, 0), (100.5, 15), (100.5, 44), 1)
    pygame.draw.line(screen, (0, 0, 0), (129, 15), (129, 44), 1)


isRuning = True
while(isRuning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    draw()
    pygame.display.flip()
