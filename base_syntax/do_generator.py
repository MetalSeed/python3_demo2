#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 16:28:58
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# generator不用向list一样创建完整列表，而是逐个推算元素，几乎不占空间
# 只要把一个列表生成式的[]改成()，就创建了一个generator
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b # tuple赋值
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 可以同过List把生成器的值都计算出来 L = list(g)
