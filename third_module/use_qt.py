#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 22:44:53
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

from PyQt5 import QtWidgets   # 导入PyQt5部件

import sys

app = QtWidgets.QApplication(sys.argv)  # 建立application对象

first_window = QtWidgets.QWidget()  # 建立窗体对象

first_window.resize(500, 400)  # 设置窗体大小

first_window.setWindowTitle("FB")  # 设置窗体标题

first_window.show()  # 显示窗体

sys.exit(app.exec())  # 运行程序
