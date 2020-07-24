#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-30 17:07:12
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# filter()的作用是从一个序列中筛出符合条件的元素。
# 由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
# Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()
