#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 21:39:07
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

classmates = ['Michael', 'Bob', 'Tracy']
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates[1] = 'Sarah'

classmates.append('Adam')
classmates.pop()
classmates.insert(1, 'Jack')
classmates.pop(1)

print('classmates =', classmates)
