#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-05 20:42:13
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))