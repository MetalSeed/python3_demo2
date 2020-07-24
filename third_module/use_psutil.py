#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-12 21:04:24
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

import psutil

# https://github.com/giampaolo/psutil
# psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，
# 还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

# CPU Memory Disks Network Sensors Processmanagement

print(psutil.cpu_count())

print(psutil.cpu_count(logical = False))

print(psutil.cpu_times())

for x in range(10):
	print(psutil.cpu_percent(interval = 1, percpu = True))