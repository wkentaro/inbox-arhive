#!/usr/bin/env python
# -*- coding: utf-8 -*-
# draw_image.py

import pygame
import sys

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('イメージの描画')

# prepare img
back_img = pygame.image.load('assets/img/moriyama.jpg').convert()     # 背景
python_img = pygame.image.load('assets/img/python.png').convert_alpha()  # 蛇

while True:
    screen.blit(back_img, (0,0))        # 背景を描画
    screen.blit(python_img, (320,400))  # 蛇を描画
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
