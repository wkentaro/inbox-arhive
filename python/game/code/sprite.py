#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sprite.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import pygame
import sys


screen_rect = pygame.Rect(0, 0, 640, 480)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pygame.Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # when bumping wall, bounce
        if self.rect.left < 0 or self.rect.right > screen_rect.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > screen_rect.height:
            self.vy = -self.vy
        # pushed down from screen
        self.rect = self.rect.clamp(screen_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    # update screen
    pygame.init()
    screen = pygame.display.set_mode(screen_rect.size)
    pygame.display.set_caption('How to use sprite')
    # create sprite
    python1 = MySprite('assets/img/python.png', 0, 0, 2, 2)
    python2 = MySprite('assets/img/python.png', 10, 10, 5, 5)
    python3 = MySprite('assets/img/python.png', 320, 240, -2, 3)
    # clock
    clock = pygame.time.Clock()
    # loop
    while True:
        clock.tick(60)  # 60fps
        # create screen
        screen.fill((0,0,255))
        # update sprite
        python1.update()
        python2.update()
        python3.update()
        # draw sprite
        python1.draw(screen)
        python2.draw(screen)
        python3.draw(screen)
        # display update
        pygame.display.update()
        # handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()