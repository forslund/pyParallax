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


from os.path import dirname, join

import pygame
from pygame.locals import *

import parallax

pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
pygame.display.set_caption('Parallax-demo')
pygame.mouse.set_visible(0)

bg = parallax.ParallaxSurface((640, 480), pygame.RLEACCEL)

directory = dirname(__file__)
bg.add(join(directory, 'p2.png'), 5)
bg.add(join(directory, 'p3.png'), 2)
bg.add(join(directory, 'p1.png'), 1)

run = True
speed = 0
t_ref = 0
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN and event.key == K_RIGHT:
            speed += 2
        if event.type == KEYUP and event.key == K_RIGHT:
            speed -= 2
        if event.type == KEYDOWN and event.key == K_LEFT:
            speed -= 4
        if event.type == KEYUP and event.key == K_LEFT:
            speed += 4

    bg.scroll(speed)  # Move the background with the set speed
    t = pygame.time.get_ticks()
    if (t - t_ref) > 60:
        bg.draw(screen)
        pygame.display.flip()
