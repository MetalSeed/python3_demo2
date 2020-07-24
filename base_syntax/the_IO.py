#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-07 20:36:04
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

# read() 读取文件的全部内容，返回str
# read(size) 最多读取size个字节的内容
# readline() 读取一行内容
# readlines() 读取所有内容并按行返回list

# with 可以自动调用close()
from datetime import datetime

with open('../test.txt', 'w', encoding = 'utf-8') as f:
    f.write('啥玩意\n')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('../test.txt', 'r', encoding = 'utf-8') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('../test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)


from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())
