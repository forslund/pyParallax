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
from math import inf

import pygame
from pygame.locals import *

import parallax

# MODE can be set to MANUAL, in which the user presses the arrow keys
# to manually scroll the image left or right, or it can be set to LEFT or RIGHT,
# to automatically scroll left or right.
MODE = "RIGHT"

scene_dimensions = (640, 480)

pygame.init()
screen = pygame.display.set_mode(scene_dimensions, pygame.DOUBLEBUF)
pygame.display.set_caption('Parallax-demo')
pygame.mouse.set_visible(0)

bg = parallax.ParallaxSurface(scene_dimensions, pygame.RLEACCEL)

image_directory = "images"

# clouds should not move at all
bg.add(join(image_directory, 'clouds.png'), inf)

# shrubs should pan 3x as fast as the mountains
bg.add(join(image_directory, 'mountains.png'), 3)
bg.add(join(image_directory, 'ground_and_shrubs.png'), 1)

run = True
scroll_speed = 0
t_ref = 0


while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        
        # Scroll speed can be adjusted below.
        # On manual mode, this block causes the scroll to move twice as quickly
        # going left vs. going right
        if MODE == "MANUAL":
            if event.type == KEYDOWN and event.key == K_RIGHT:
                scroll_speed += 2
            if event.type == KEYUP and event.key == K_RIGHT:
                scroll_speed -= 2
            if event.type == KEYDOWN and event.key == K_LEFT:
                scroll_speed -= 4
            if event.type == KEYUP and event.key == K_LEFT:
                scroll_speed += 4
        elif MODE == "LEFT":
            scroll_speed = -4
        elif MODE == "RIGHT":
            scroll_speed = 4
        else:
            raise Exception("MODE must be set to either MANUAL, LEFT, or RIGHT")

    bg.scroll(scroll_speed)  # Move the background with the set scroll_speed
    t = pygame.time.get_ticks()
    if (t - t_ref) > 60:
        bg.draw(screen)
        pygame.display.flip()
