#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import (
    print_function,
    division,
    unicode_literals,
    )
import itertools

import cv2
import numpy as np

def drawMatches(img1, kp1, img2, kp2, matches):
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]
    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')
    out[:rows1,:cols1,:] = np.dstack([img1, img1, img1])
    out[:rows2,cols1:cols1+cols2,:] = np.dstack([img2, img2, img2])
    for mat in matches:
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)
    cv2.imshow('Matched Features', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    imgs = []
    for i in xrange(3):
        img = cv2.imread('frame{}.png'.format(str(i).zfill(4)))
        dsize = (int(img.shape[1]*0.4), int(img.shape[0]*0.4))
        img = cv2.resize(img, dsize)
        imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        imgs.append(imgray)
        del img

    sift = cv2.SIFT()
    matcher = cv2.DescriptorMatcher_create('FlannBased')
    for img1, img2 in itertools.combinations(imgs, 2):
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
        matches = matcher.match(des1, des2)
        yield matches
        good_maches = [dmatch for dmatch in matches if dmatch.distance < 100]
        drawMatches(img1, kp1, img2, kp2, good_maches)

main()
