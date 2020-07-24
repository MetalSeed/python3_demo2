#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 12:33:37
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$


print([x * x for x in range(1, 11)])
# 筛选
print([x * x for x in range(1, 11) if x % 2 == 0])
# 全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


import os
L = [d for d in os.listdir('.')]

print(L)

L1 = [1, 2, 3]
L2 = [3, 5, 7]
L3 = [x + y for x, y in zip(L1, L2)]
print(L3)