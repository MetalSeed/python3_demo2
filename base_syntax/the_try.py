#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 20:24:18
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
# try except可以跨层捕捉，非常方便
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查
# 如果不知如何处理错误，就继续上抛，最外层如果有没被捕捉的raise，将被调用端捕捉

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('QAQ invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!', e)
        raise 

def main():
	try:
		bar()
	except Exception as e:
		print('Exception:', e)

main()
print('END')








