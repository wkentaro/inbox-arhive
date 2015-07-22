#!/usr/bin/env python
# -*- coding: utf-8 -*-
# draw_figure.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import pygame

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("図形の描画")

while True:
    screen.fill((0,0,0))

    # 図形を描画
    # 黄の矩形
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(10,10,300,200))
    # 赤の円
    pygame.draw.circle(screen, (255,0,0), (320,240), 100)
    # 紫の楕円
    pygame.draw.ellipse(screen, (255,0,255), (400,300,200,100), 1)
    # 白い線
    pygame.draw.line(screen, (255,255,255), (0,0), (640,480))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
