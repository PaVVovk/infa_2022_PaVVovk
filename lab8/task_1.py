import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

clr = {"white": (255, 255, 255),
       "yellow": (250, 255, 1),
       "red": (255,0,0),
       "black": (0,0,0)}

xc = 200
yc = 200

circle(screen, clr["yellow"], (xc, yc), 100)
circle(screen, clr["white"], (xc+35, yc-25), 20)
circle(screen, clr["white"], (xc-35, yc-25), 20)
circle(screen, clr["black"], (xc-35, yc-25), 10)
circle(screen, clr["black"], (xc+35, yc-25), 10)
polygon(screen, clr["red"], [(xc-50,yc+55),(xc+50,yc+55),
                             (xc,yc+10)])
line(screen,clr["black"], (xc-40,yc-80), (xc-15,yc-50))
line(screen,clr["black"], (xc+40,yc-80), (xc+15,yc-50))
polygon(screen, clr["black"], [(xc-50,yc+55),(xc+50,yc+55),
                             (xc,yc+10)],1)
circle(screen, clr["black"], (xc+35, yc-25), 20,1)
circle(screen, clr["black"], (xc-35, yc-25), 20,1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
