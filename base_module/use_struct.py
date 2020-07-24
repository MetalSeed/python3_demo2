#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 15:31:26
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

# bytes to string/int
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
# pack 把数据类型变为字节， unpack把字节变成数据类型
import struct
s = struct.pack('>I', 10240099)
print(s)
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数(uint)和H：2字节无符号整数。
s = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(s)