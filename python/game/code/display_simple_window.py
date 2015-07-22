#!/usr/bin/env python
# -*- coding: utf-8 -*-
# display_simple_window.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import pygame
from pygame.locals import *


def create_simple_window():
    # Initialize pygame
    pygame.init()
    # Create window with size of screen_size
    screen_size = (640, 480)
    screen = pygame.display.set_mode(screen_size)
    # set title bar caption
    pygame.display.set_caption(u'Create Window')

    # game loop
    while True:
        screen.fill((0, 0, 255))  # set color to window
        pygame.display.update()   # update the window
        # process the events
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == '__main__':
    create_simple_window()