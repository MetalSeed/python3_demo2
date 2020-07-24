# 在Python中，一个.py文件就称之为一个模块（Module）
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）,__init__.py 用来指定包结构
# mycompany
#  ├─ web
#  │  ├─ __init__.py
#  │  ├─ utils.py
#  │  └─ www.py
#  ├─ __init__.py
#  ├─ abc.py
#  └─ xyz.py
# 文件www.py的模块名就是mycompany.web.www
# 在环境变量 PYTHONPATH 中增加路径即可搜索到
# Anaconda 第三方模块管理工具，Anaconda会把系统Path中的python指向自己自带的Python，
# 并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录

# 模块模板

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '
# 使用__author__变量把作者写进去
__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们在命令行运行hello模块文件时。会调用test() （Python解释器把一个特殊变量__name__置为__main__）
if __name__=='__main__':
	test()
