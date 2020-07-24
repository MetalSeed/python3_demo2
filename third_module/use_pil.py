#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-12 19:04:14
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 16:14:39
# @Author  : MetalSeed (=.=)
# @Link    :  
# @Version : $Id$

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('1.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))

box1 = (0, 0, 2000, 2000)
box2 = (1000, 0, 3000, 2000)

im1 = im.crop(box1)
im2 = im.crop(box2)

# im1.show()
# im2.show()

imo = Image.alpha_composite(im1, im2)
imo.show()

