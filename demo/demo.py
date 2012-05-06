import os, sys
import pygame
from pygame.locals import *

sys.path.append ("../lib")
import parallax

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Parallax-test')
pygame.mouse.set_visible(0)

bg = parallax.parallaxSurface()
bg.addLevel('p2.png', 2)
bg.addLevel('p1.png', 1)

while True:
    bg.draw(screen)
    pygame.display.flip()
    bg.scroll(2)

