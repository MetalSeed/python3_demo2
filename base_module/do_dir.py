#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-07 21:29:15
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import os
from datetime import datetime

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# os.environ 操作系统中定义的环境变量
# os.environ.get('key') 获取某个环境变量的值
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
ndir = os.path.join('/Users/MetalSeed/Documents/CodeBox/Python', 'testdir')
# 然后创建一个目录:
os.mkdir(ndir)
# 删掉一个目录:
os.rmdir(ndir)

# os.path.split() 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# os.path.splitext('/path/to/file.txt') 得到文件扩展名


# os.rename('../test.txt', '../test.py')
# os.remove('../test.py')

# copyfile() 在shutil模块
import re

# L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
L = [x for x in os.listdir('.') if re.match(r'\w*\.py', x)]
print(L)
