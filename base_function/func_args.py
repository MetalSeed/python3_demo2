#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 00:04:52
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。(网页注册是可选项用命名关键字)

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。



# 默认参数降低了函数定义和调用的难度。无论是简单调用还是复杂调用，函数只需要定义一个
# 当不按顺序提供部分默认参数时，需要把参数名写上 enroll('Adam', 'M', city='Tianjin')
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))


# Python函数在定义的时候，默认参数L的值就被计算出来了，默认参数必须指向不变对象！
# 每次调用该函数，如果改变了他的内容，则下次调用时，默认参数的内容就变了。
def add_end(L=[]):
    L.append('END')
    return L

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 调用从calc([1, 2, 3]) 简化成 calc(1, 2, 3)，不用预先装list或tuple
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

# *names表示把names这个list的所有元素作为可变参数传进去，函数内部收到的是一个tuple
names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')



def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)



# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f2(*args, **kw)
