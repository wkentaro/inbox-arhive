#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sound_test.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import pygame
import sys

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('サウンドテスト')

# load img
img = pygame.image.load('assets/img/python.png').convert_alpha()
img_rect = img.get_rect()

# load sound
hit_sound = pygame.mixer.Sound('assets/audio/hit.wav')

vx = vy = 300  # 1 sec moving pixel
clock = pygame.time.Clock()

# play BGM
pygame.mixer.music.load('assets/audio/tam-n11.wav')
pygame.mixer.music.play(-1)

while True:
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.


    # move img
    img_rect.x += vx * time_passed_seconds
    img_rect.y += vy * time_passed_seconds

    # bounce by hitting the wall 
    if img_rect.left < 0 or img_rect.right > screen_size[0]:
        hit_sound.play()  # play sound
        vx = -vx
    elif img_rect.top < 0 or img_rect.bottom > screen_size[1]:
        hit_sound.play()  # play sound
        vy = -vy

    screen.fill((0,0,255))
    screen.blit(img, img_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()