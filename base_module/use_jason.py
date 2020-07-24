#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-09 21:20:20
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import json

# json.dumps()方法把任意对象序列化成一个bytes
# json.dump()把对象序列化后写入一个file-like Object
# json.load()从一个file-like Object中直接反序列化出对象。
# json.loads()从string中反序列化出对象

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
# 传入default函数，先把object转换成dict, 再将dick序列化
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

# loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
