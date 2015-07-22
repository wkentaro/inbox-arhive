#!/usr/bin/env python
# -*- coding: utf-8 -*-
# chara_anime.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import pygame
import sys

screen_rect = pygame.Rect(0, 0, 640, 480)


def load_image(filename, colorkey=None):
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image


def split_image(image):
    """32x128 character image is splitted to 32x32 4 images
    and return splitted images as list"""
    image_list = []
    for i in range(0, 128, 32):
        surface = pygame.Surface((32,32))
        surface.blit(image, (0,0), (i,0,32,32))
        surface.set_colorkey(surface.get_at((0,0)), pygame.RLEACCEL)
        surface.convert()
        image_list.append(surface)
    return image_list

class Character(pygame.sprite.Sprite):
    animcycle = 12  # speed of animation
    frame = 0
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = split_image(load_image(filename))
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self):
        # character animation
        self.frame += 1
        self.image = self.images[self.frame/self.animcycle % 4]


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_rect.size)
    pygame.display.set_caption('キャラクターアニメーション')

    all = pygame.sprite.RenderUpdates()
    Character.containers = all

    player = Character('assets/img/player4.png', 0, 0)
    king = Character('assets/img/king4.png', 32, 0)
    soldier = Character('assets/img/soldier4.png', 64, 0)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0,0,255))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()