#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput

lines = fileinput.input()

for line in lines:
    a, x = map(int, line.split(' '))
    if a == 0 and x == 0:
        break
    a = int(a % 1e8)

    ans = 1
    count = 0
    step = int(x / a)
    while True:
        if count+step > x:
            y = x - count
            count += y
        else:
            y = step
            count += y

        ans *= int(str(a**y)[-8:])
        ans = int(str(ans)[-8:])

        if count >= x:
            break

    print(ans)
