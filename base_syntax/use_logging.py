#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-09 21:38:28
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import logging
logging.basicConfig(level=logging.INFO)


# logging 允许指定记录信息的级别(debug，info，warning，error)
# logging 一条语句可以同时输出到不同的地方，比如console和文件

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
