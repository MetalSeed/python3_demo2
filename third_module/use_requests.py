#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-12 20:49:45
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import requests

# requests。它是一个Python第三方库，处理URL资源特别方便。
url = 'http://www.baidu.com'
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies = cs, timeout = 2.5)

print(r.text)
