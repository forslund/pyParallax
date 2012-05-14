'''A simple parallax rendering module'''
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

class parallaxSubSurface:
	def __init__(self, s, f):
		self.scroll = 0
		self.factor = f
		self.surface = s

class parallaxSurface:
	'''Class handling parallax scrolling of a series of surfaces'''
	def __init__(self):
		print "parllaxSurface inited!"
		self.numLevels = 0
		self.scroller = 0
		self.parallaxLevels = []
	def addLevel(self, imagePath, scrollFactor):
		'''Adds a parallax level, first added level is the 
		   deepest level, i.e. furthest back into the \"screen\".

		   imagePath is the path to the image to be used
		   scrollFactor is the slowdown factor for this parallax level.'''
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
		''' This draws all parallax levels to the surface provided as argument'''
		sWidth  = surface.get_width()
		sHeight = surface.get_height()

		for l in self.parallaxLevels:
			surface.blit(l.surface, (0,0), (l.scroll, 0, sWidth, sHeight))
			surface.blit(l.surface, (l.surface.get_width() - l.scroll, 0), (0, 0, l.scroll, sHeight))

	def scroll(self, offset):
		'''scroll moves each surface _offset_ pixels / assigned factor'''
		self.scroller = (self.scroller + offset)
		for l in self.parallaxLevels:
			l.scroll = (self.scroller / l.factor) % l.surface.get_width()

