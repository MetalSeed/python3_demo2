#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 15:24:53
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
