#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 22:22:20
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 20:
    acc = acc * n
    n = n + 1
    if n == 10:
    	break
print(acc)
