# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:35:20 2022

@author: longzheng
"""
'''从网上找到的方法，从这个方法可以看出，numpy的切片可能是分片切的，
先切行，在切列这样子,所以得到了行或者列，可以对它们再次排序,不过方向好像有点问题'''

import numpy as np
A = np.arange(25).reshape(5,5)
A2 = A[:,[4,1,2,3,0]] 
A3 = A[[4,1,2,3,0],:]
