# -*- coding: utf-8 -*-
#    Copyright (C) , 2012 Åke Forslund (ake.forslund@gmail.com)
#
#    Permission to use, copy, modify, and/or distribute this software for any
#    purpose with or without fee is hereby granted, provided that the above
#    copyright notice and this permission notice appear in all copies.
#
#    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#


import os, sys
import pygame
from pygame.locals import *

SCREENRECT = Rect(0,0, 640, 480)

class parallaxSubSurface:
	def __init__(self, s, f):
		self.scroll = 0
		self.factor = f
		self.surface = s

class parallaxSurface:
	def __init__(self):
		print "parllaxSurface inited!"
		self.numLevels = 0
		self.scroller = 0
		self.parallaxLevels = []
	def addLevel(self, imagePath, scrollFactor):
		try:
			image = (pygame.image.load(imagePath))
		except:
			print "couldn't open image:", imagePath
			raise SystemExit, message

		image.set_colorkey((0xff,0x00,0xea))
		image = image.convert()
		self.parallaxLevels.append(parallaxSubSurface(image, scrollFactor))
		self.numLevels += 1

	def draw(self, surface):
		i = 0
		for l in self.parallaxLevels:
			surface.blit(l.surface, (0,0), (l.scroll, 0, SCREENRECT.width, SCREENRECT.height))
			surface.blit(l.surface, (l.surface.get_width() - l.scroll, 0), (0, 0, l.scroll, SCREENRECT.height))
			i += 1

	def scroll(self, offset):
		self.scroller = (self.scroller + offset)
		for l in self.parallaxLevels:
			l.scroll = (self.scroller / l.factor) % l.surface.get_width()

