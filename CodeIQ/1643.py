#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput

lines = fileinput.input()


def lower_some_num(x, n=8):
    # assert type(x) == int
    return int(str(x)[-n:])


def power(x, n):
    x = lower_some_num(x)
    if n == 0:
        return 1
    elif n % 2 == 0:
        ret = power(x**2, n/2)
        return lower_some_num(ret)
    else:
        ret = x * power(x, n-1)
        return lower_some_num(ret)


for line in lines:
    a, x = map(int, line.split(' '))
    if a == 0 and x == 0:
        break
    ans = power(a, x)
    print(ans)
