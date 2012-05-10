import os, sys
import pygame
from pygame.locals import *

SCREENRECT = Rect(0,0, 640, 480)

class parallaxSurface:
	def __init__(self):
		print "parllaxSurface inited!"
		self.numLevels = 0
		self.parallaxSurfaces = []
		self.sc = []
		self.factor = []
		self.scroller = 0
	def addLevel(self, imagePath, scrollFactor):
		try:
			image = (pygame.image.load(imagePath))
		except:
			print "couldn't open image:", imagePath
			raise SystemExit, message

		image.set_colorkey((0xff,0x00,0xea))
		image = image.convert()
		self.parallaxSurfaces.append(image)
		self.factor.append(scrollFactor)
		self.sc.append(0)
		self.numLevels += 1

	def draw(self, surface):
		i = 0
		for s in self.parallaxSurfaces:
			surface.blit(s, (0,0), (self.sc[i], 0, SCREENRECT.width, SCREENRECT.height))
			surface.blit(s, (s.get_width() - self.sc[i], 0), (0, 0, self.sc[i], SCREENRECT.height))
			i += 1

	def scroll(self, offset):
		self.scroller = (self.scroller + offset)
		for i in range(len(self.sc)):
			self.sc[i] = (self.scroller / self.factor[i]) % self.parallaxSurfaces[i].get_width()

