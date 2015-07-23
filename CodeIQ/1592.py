#!/usr/bin/env python
# -*- coding: utf-8 -*-


# code = '169 147 161 173 145 161 67 159 149 67 171 133 153 133 161 169 133 159 67 137 147 161 173 151 161 173 67 139 141'
code = raw_input()
codes = map(int, code.split(' '))

ret = map(lambda x: (x-3)/2, codes)
ret = map(chr, ret)
print(''.join(ret))