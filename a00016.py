# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
abc = np.linspace(0,1,11)
print(f'{abc}\n{abc.shape}\n{abc.size}')

abcd = np.arange(5, 21, 51)
print(abcd)
print(np.arange(1, 21).reshape(2, 10))

abcde = np.arange(5, 21, 2)
print(abcde)
print(np.arange(1, 21).reshape(2,10))

abcdef = np.linspace(0, 1, 10)
print(f'{abcdef}\n{abcdef.shape}\n{abcde.size}')

import numpy as np


xy = np.array([[1,2],[3,4],[5,6]])
xx = np.array([[3,4],[5,6],[7,8]])
print(f'xy.shpae, xx.shape')
print(f'{xy + xx}\n {xy*2}')

print(np.add(xy,xx))
print(np.subtract(xy,xx)) # elemnet - wise subrtraction
print(np.multiply(xy,xx)) # mulltiplication
print(np.sqrt(xy)) #root

print(xy.shape, xx.shape)
print(f'{xy+xx}\n{xy*2}')

import numpy as np
import math
xyzz = np.ones((2,1))
xyz = np.zeros((2,1))
print(xyz)
print(xyz, xyz.shape, xyz.ndim)
print(np.dot(xyz,xyzz))

xd =np.array([[1,2],[1,2]]); print(xd)
print(xd.dot(xyz));print(np.dot(xd,xyz))

print(xd.T)
print((xd+3))
print(xd)
xd += 3 
print(xd)

print(np.add(xd,xyz))
print(np.subtract(xd,xyz))
print(np.multiply(xyz,xd))

np.common_type(xd)
print(xd)
np.fabs(xd)



