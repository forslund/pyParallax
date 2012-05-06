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

run = True
speed = 0
while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			run = False
		if event.type == KEYDOWN and event.key == K_RIGHT:
			speed += 5
		if event.type == KEYUP and event.key == K_RIGHT:
			speed -= 5
		if event.type == KEYDOWN and event.key == K_LEFT:
			speed -= 5
		if event.type == KEYUP and event.key == K_LEFT:
			speed += 5
		
	bg.scroll(speed)
	bg.draw(screen)
	pygame.display.flip()

