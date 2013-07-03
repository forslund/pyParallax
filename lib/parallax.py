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

import pygame

class _subsurface:
    '''Container class for subsurface'''
    def __init__(self, surface, factor):
        self.scroll = 0
        self.factor = factor
        self.surface = surface

class ParallaxSurface:
    '''Class handling parallax scrolling of a series of surfaces'''
    def __init__(self, size, colorkey_flags = 0):
        print "parllaxSurface inited!"
        self.colorkey_flags = colorkey_flags
        self.scroller = 0
        self.levels = []
        self.size = size

    def add(self, image_path, scroll_factor):
        '''Adds a parallax level, first added level is the
           deepest level, i.e. furthest back into the \"screen\".

           image_path is the path to the image to be used
           scroll_factor is the slowdown factor for this parallax level.'''
        try:
            image = (pygame.image.load(image_path))
        except:
            message = "couldn't open image:" + image_path
            raise SystemExit, message
        image = image.convert()
        if len(self.levels) > 0:
            image.set_colorkey((0xff, 0x00, 0xea), self.colorkey_flags)
        self.levels.append(_subsurface(image, scroll_factor))

    def add_surface(self, surface, scroll_factor):
        surface = surface.convert()
        if len(self.levels) > 0:
            surface.set_colorkey((0xff, 0x00, 0xea), self.colorkey_flags)
        self.levels.append(_subsurface(surface, scroll_factor))

    def draw(self, surface):
        ''' This draws all parallax levels to the surface
            provided as argument '''
        s_width  = self.size[0]
        s_height = self.size[1]

        for lvl in self.levels:
            surface.blit(lvl.surface, (0, 0),
                        (lvl.scroll, 0, s_width, s_height))
            surface.blit(lvl.surface,
                        (lvl.surface.get_width() - lvl.scroll, 0),
                         (0, 0, lvl.scroll, s_height))

    def scroll(self, offset):
        '''scroll moves each surface _offset_ pixels / assigned factor'''
        self.scroller = (self.scroller + offset)
        for lvl in self.levels:
            lvl.scroll = (self.scroller / lvl.factor) % lvl.surface.get_width()

