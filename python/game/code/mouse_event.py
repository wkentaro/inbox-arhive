#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mouse_event.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import pygame

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('マウスイベント')

back_img = pygame.image.load('assets/img/moriyama.jpg').convert()
python_img = pygame.image.load('assets/img/python.png').convert_alpha()

cur_pos = (0,0)   # python pos
pythons_pos = []  # copied python pos list

while True:
    screen.blit(back_img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # copy python with mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            x -= python_img.get_width() / 2
            y -= python_img.get_height() / 2
            pythons_pos.append((x,y))  # add python pos
        # move python with mouse move
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            x -= python_img.get_width() / 2
            y -= python_img.get_height() / 2
            cur_pos = (x,y)

    # display python
    screen.blit(python_img, cur_pos)
    for i, j in pythons_pos:
        screen.blit(python_img, (i,j))

    pygame.display.update()
