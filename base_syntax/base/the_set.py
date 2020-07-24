#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 22:32:30
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# 注意 set是无序的

s1 = set([3, 3, 2, 2, 1, 1])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

s1.add(5)
s1.remove(2)
print(s1)