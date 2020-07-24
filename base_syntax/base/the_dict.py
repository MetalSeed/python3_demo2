#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 22:31:55
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：
# 1 查找和插入的速度极快，不会随着key的增加而变慢；
# 2 需要占用大量的内存，内存浪费多。

# 而list相反：
# 1 查找和插入的时间随着元素的增加而增加；
# 2 占用空间小，浪费内存很少。

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

d['gf'] = 20
print(d['gf'])
d.pop('gf')
print(d.get('gf'))

print('d[\'Michael\'] =', d['Michael'])
