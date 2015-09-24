#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right

a = [2, 5, 8, 9, 10]
x = 8

i_left = bisect_left(a, x)
print i_left
print a[i_left]

i_right = bisect_right(a, x)
print i_right
print a[i_right]