#!/usr/bin/env python
# -*- coding: utf-8 -*-


def process(string):
    if ord(string[0]) % 15 == 0:
        return string.capitalize()
    elif ord(string[0]) % 5 == 0:
        return string.upper()
    elif ord(string[0]) % 3 == 0:
        return string.lower()
    return string

line = raw_input()
print process(line)