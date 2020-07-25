#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-05 21:59:32
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import functools

# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
    @functools.wraps(func)
    # def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

# functools.wraps 相当于 wrapper.__name__ = func.__name__
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)
