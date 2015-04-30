#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt

this_dir = os.path.join(os.path.dirname(__file__))

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = os.path.join(this_dir, 'bin0001.jpg')
img = cv2.imread(filename)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
_, s, _ = cv2.split(img_hsv)
# plt.imshow(s, cmap='gray')

ret, thresh = cv2.threshold(s, 30, 255, cv2.THRESH_BINARY)
# plt.imshow(thresh, cmap='gray')
# plt.show()

kernel = np.ones((3,3), np.uint8)
# dilation = cv2.dilate(thresh, kernel, iterations=30)
# # plt.imshow(dilation, cmap='gray')
# erosion = cv2.erode(dilation, kernel, iterations=30)
# plt.imshow(erosion, cmap='gray')
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=30)

# ----------
# upper bar
# ----------
found_min, found_max = False, False
x_center = morph.shape[1]/2
for i, row in enumerate(morph):
    if not found_min:
        if row[x_center] == 0:
            y_min = i
            found_min = True
    elif not found_max:
        if row[x_center] == 255:
            y_max = i
            found_max = True
    else:
        break
upper_bar_center = (y_max + y_min) / 2

# ----------
# lower bar
# ----------
found_min, found_max = False, False
for i, row in enumerate(morph[::-1]):
    if not found_min:
        if row[x_center] == 0:
            y_min = morph.shape[0] - i
            found_min = True
    elif not found_max:
        if row[x_center] == 255:
            y_max = morph.shape[0] - i
            found_max = True
    else:
        break
lower_bar_center = (y_max + y_min) / 2

y_center = (upper_bar_center+lower_bar_center)/2

# ----------
# right bar
# ----------
right_bar_pos = None
tmp = np.where(morph[y_center, x_center:] == 0)[0]
if len(tmp) != 0:
    right_bar_pos = x_center + min(tmp)
del tmp

# ---------
# left bar
# ---------
left_bar_pos = None
tmp = np.where(morph[y_center, :x_center] == 0)[0]
if len(tmp) != 0:
    left_bar_pos = min(tmp)
del tmp

morph_bgr = cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR)
cv2.line(morph_bgr, (0, upper_bar_center), (morph_bgr.shape[1], upper_bar_center), (0,255,0), 30)
cv2.line(morph_bgr, (0, lower_bar_center), (morph_bgr.shape[1], lower_bar_center), (0,255,0), 30)
if right_bar_pos:
    cv2.line(morph_bgr, (right_bar_pos, 0), (right_bar_pos, morph_bgr.shape[0]), (0,255,0), 30)
if left_bar_pos:
    print left_bar_pos
    cv2.line(morph_bgr, (left_bar_pos, 0), (left_bar_pos, morph_bgr.shape[0]), (0,255,0), 30)
cv2.circle(morph_bgr, (x_center, y_center), 10, (255,0,0), 30)

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(morph_bgr)
plt.show()
