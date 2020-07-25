#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 23:53:54
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import math

def function():
	pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# TypeError: bad operand type:
# my_abs('123')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 函数可以同时返回多个值，但其实就是一个tuple
# 多个变量可以同时接收一个tuple，按位置赋给对应的值
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# 因为函数没有名字，不必担心函数名冲突
lambda x: x * x
def f(x):
    return x * x

# 可以把匿名函数赋值给一个变量，也可以把匿名函数作为返回值返回
f = lambda x: x * x

