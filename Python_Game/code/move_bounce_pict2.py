#!/usr/bin/env python
# -*- coding: utf-8 -*-
# move_bounce_pict2.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys
import pygame

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('画像の移動と跳ね返り処理2')

img = pygame.image.load('assets/img/python.png').convert_alpha()
img_rect = img.get_rect()

vx = vy = 120  # 1 second move pixel
clock = pygame.time.Clock()

while True:
    time_passed = clock.tick(60)  # 60fps
    time_passed_seconds = time_passed / 1000.0  # convert milisec -> sec

    # move img
    img_rect.x += vx * time_passed_seconds
    img_rect.y += vy * time_passed_seconds
    # boucing
    if img_rect.left < 0 or img_rect.right > screen_size[0]:
        vx = -vx
    if img_rect.top < 0 or img_rect.bottom > screen_size[1]:
        vy = -vy

    screen.fill((0,0,255))
    screen.blit(img, img_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()