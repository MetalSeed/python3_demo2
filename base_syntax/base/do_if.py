#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 21:46:17
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
