#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-05 21:37:42
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import functools

# 使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数