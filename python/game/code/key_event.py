#!/usr/bin/env python
# -*- coding: utf-8 -*-
# key_event.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import pygame
import sys

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('キーイベント')

img = pygame.image.load('assets/img/python.png').convert_alpha()
img_rect = img.get_rect()
img_rect.center = (320, 240)

vx = vy = 10  # moving distance with key pushing

while True:
    screen.fill((0,0,255))
    screen.blit(img, img_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # ESCキーならスクリプトを終了
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            # 矢印キーなら画像を移動
            if event.key == pygame.K_LEFT:
                img_rect.move_ip(-vx, 0)
            if event.key == pygame.K_RIGHT:
                img_rect.move_ip(vx, 0)
            if event.key == pygame.K_UP:
                img_rect.move_ip(0, -vy)
            if event.key == pygame.K_DOWN:
                img_rect.move_ip(0, vy)