#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 15:54:53
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，
# 而是Iterator，只有用for循环迭代的时候才真正计算。

import itertools


natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

#just caculate next object when been called
# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('abc')
# for c in cs:
# 	print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('abc', 3)
# for n in ns:
# 	print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('abc', '123'):
	print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBBCCCDD'):
	print(key, list(group))

for key, group in itertools.groupby('AaabBbcCaa', lambda c: c.upper()):
	print(key, list(group))


# 限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

