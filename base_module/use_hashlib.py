#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 15:40:26
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# 摘要算法是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
# 摘要算法之所以能指出数据是否被篡改过，是因为摘要函数是一个单向函数，计算f(data)很容易，
# 但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。
# 此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# 标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，
# 因为针对相同的message，不同的key会产生不同的hash。
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
