#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 12:14:30
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 0可以省略，list tuple string都支持切片
print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
