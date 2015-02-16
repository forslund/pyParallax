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

'''A simple parallax rendering module'''

import pygame

class _subsurface(object):
    '''Container class for subsurface'''
    def __init__(self, surface, factor):
        self.scroll = 0
        self.factor = factor
        self.surface = surface

class ParallaxSurface(object):
    '''Class handling parallax scrolling of a series of surfaces'''
    def __init__(self, size, colorkey_flags=0):
        self.colorkey_flags = colorkey_flags
        self.scroller = 0
        self.levels = []
        self.levels_id = {}
        self.size = size
        self.orientation = 'horizontal'

    def chg_size(self, size):
        ''' Changes the parallax surface's size. '''
        self.size = size

    def update(self, image_path, scroll_factor, size=(0, 0)):
        ''' Updates the parallax level identified by image_path and
            redefines the layer's scroll_factor and the size of the entire
            parallax surface. '''
        self.rem(image_path)
        self.add(image_path, scroll_factor, size)

    def rem(self, image_path):
        ''' Removes the parallax level created from the image_path.
            If no matching level is found nothing is removed. '''
        if image_path in self.levels_id:
            elem_id = self.levels_id[image_path]
            del self.levels[elem_id]
            del self.levels_id[image_path]

    def add(self, image_path, scroll_factor, size=None):
        ''' Adds a parallax level, first added level is the
            deepest level, i.e. furthest back into the \"screen\".

            image_path is the path to the image to be used
            scroll_factor is the slowdown factor for this parallax level. '''
        try:
            image = (pygame.image.load(image_path))
        except:
            message = "couldn't open image:" + image_path
            raise SystemExit, message
        if ".png" in image_path:
            image = image.convert_alpha()
        else:
            image = image.convert()
        if len(self.levels) > 0:
            image.set_colorkey((0xff, 0x00, 0xea), self.colorkey_flags)
        if size is not None:
            image = pygame.transform.scale(image, size) # Change the image size
            self.chg_size(size) # Update the size
        # Track the current image by it id
        self.levels_id[image_path] = len(self.levels)
        self.levels.append(_subsurface(image, scroll_factor))

    def add_colorkeyed_surface(self, surface, scroll_factor,
                               color_key=(0xff, 0x00, 0xea)):
        ''' Adds a colorkeyed surface created elsewhere. '''
        surface = surface.convert()
        if len(self.levels) > 0:
            surface.set_colorkey(color_key, self.colorkey_flags)
        self.levels.append(_subsurface(surface, scroll_factor))

    def add_surface(self, surface, scroll_factor):
        ''' Adds a surface created elsewhere. '''
        surface = surface.convert_alpha()
        if len(self.levels) > 0:
            surface.set_colorkey((0xff, 0x00, 0xea), self.colorkey_flags)
        self.levels.append(_subsurface(surface, scroll_factor))

    def draw(self, surface):
        ''' This draws all parallax levels to the surface
            provided as argument. '''
        s_width = self.size[0]
        s_height = self.size[1]
        for lvl in self.levels:
            if self.orientation == 'vertical':
                surface.blit(lvl.surface, (0, 0),
                             (0, -lvl.scroll, s_width, s_height))
                surface.blit(lvl.surface,
                             (0, lvl.scroll - lvl.surface.get_height()))
            else:
                surface.blit(lvl.surface, (0, 0),
                             (lvl.scroll, 0, s_width, s_height))
                surface.blit(lvl.surface,
                             (lvl.surface.get_width() - lvl.scroll, 0),
                             (0, 0, lvl.scroll, s_height))

    def scroll(self, offset, orientation=None):
        '''scroll moves each surface _offset_ pixels / assigned factor'''
        if orientation is not None:
            self.orientation = orientation

        self.scroller = (self.scroller + offset)
        for lvl in self.levels:
            if self.orientation == 'vertical':
                lvl.scroll = (self.scroller / lvl.factor) \
                             % lvl.surface.get_height()
            else:
                lvl.scroll = (self.scroller / lvl.factor) \
                             % lvl.surface.get_width()

class VerticalParallaxSurface(ParallaxSurface):
    ''' Class implementing vertical scrolling parallax surface. '''
    def __init__(self, size, colorkey_flags=0):
        ParallaxSurface.__init__(self, size, colorkey_flags)
        self.orientation = 'vertical'
