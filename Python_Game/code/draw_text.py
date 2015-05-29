#!/usr/bin/env python
# -*- coding: utf-8 -*-
# draw_text.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import pygame


screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Hello, world!')

# create font
sysfont = pygame.font.SysFont(None, 80)
# create surface with text
hello1 = sysfont.render('Hello, world!', False, (0,0,0))
hello2 = sysfont.render('Hello, world!', True, (0,0,0))
hello3 = sysfont.render('Hello, world!', True, (255,0,0), (255,255,0))

while True:
    screen.fill((0,0,255))

    # draw text
    screen.blit(hello1, (20,50))
    screen.blit(hello2, (20,150))
    screen.blit(hello3, (20,250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
