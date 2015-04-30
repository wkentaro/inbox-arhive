#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt


if len(sys.argv) < 3:
    quit()

mask = cv2.imread('mask2.jpg')
img1 = cv2.imread(sys.argv[1])
img1[mask==0] = 0
img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img1_hsv)
h1 = h

img2 = cv2.imread(sys.argv[2])
img2[mask==0] = 0
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img2_hsv)
h2 = h

diff = cv2.absdiff(h1, h2)
mask2 = np.zeros_like(diff, np.uint8)
diff[cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) == 0] = 255
mask2[diff < 10] = 255
kernel = np.ones((2,2), np.uint8)
# mask3 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel, iterations=1)
mask3 = cv2.dilate(mask2, kernel, iterations=1)
mask3 = cv2.erode(mask3, kernel, iterations=1)
print('white: {0}'.format(mask2.astype(bool).sum()))
print('white: {0}'.format(mask3.astype(bool).sum()))

plt.subplot(221)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.subplot(222)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.subplot(223)
plt.imshow(mask2, cmap='gray')
plt.subplot(224)
plt.imshow(mask3, cmap='gray')
plt.savefig('compare.png')


# diff = cv2.absdiff(img1, img2)
# mask2 = np.zeros_like(diff)
# mask2[diff<5] = 255
#
# kernel = np.ones((3,3), np.uint8)
# mask3 = cv2.dilate(mask2, kernel, iterations=10)
# mask3 = cv2.erode(mask3, kernel, iterations=10)
# print("white: {0}".format(mask3.astype(bool).sum()))
#
# plt.subplot(221)
# plt.imshow(img1, cmap='gray')
# plt.subplot(222)
# plt.imshow(img2, cmap='gray')
# plt.subplot(223)
# plt.imshow(mask2, cmap='gray')
# plt.subplot(224)
# plt.imshow(mask3, cmap='gray')
# plt.show()
