# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd 
import math

xa = np.array([[1,2],[3,4],[5,6]])
xb = np.array([[3,4],[5,6],[7,8]])

print(xa.shape, xb.shape)
print(f'{xa+xb}\n{xa*2}')

xd = np.array([[1,2],[1,2]]); print(xd)
print(np.dot(xa,xd));print(np.dot(xb,xd))

ya = np.arange(1,10).reshape(3,3); print(ya)
ya1 = np.ones((3,1)); print(ya1)
yb = ya + ya1; print(yb)
ya2 = np.full((1,3),2); print(ya2)
yc = ya+ya2; print(yc)

print(yc.sum(), yc.mean(), yc.min(), yc.max(), yc.var(), yc.std())

t = np.arange(21).reshape(3,7); print(t)
print(t[0], t[0:4])
print(t[:2])
print(t[:2,:3])

t1 = np.arange(0,50)
ta1 = np.arange(0, 50000)
print(ta1.ndim)
t2 = np.argmax(t1)
t3 = np.argmin(t1)
print(t1.mean(axis=0))
print(t1.mean(axis=0))
print(t1.sum(), t1.mean(), t1.min(), t1.max(), t1.var(), t1.std)


print(t2)
print(t1)
print(t3)

def ott:
    for i in j:
        for j in t1:
            sum = t1 + j + i
return sum

a1(5)

att = np.arange(5,500)
sum = []

class ott:
    for i in att:
            sum = i + att

ott(50)
print(ott(50))

i = input()

class dumb:
    print(f'i.min:{i.max()}')

karray = np.arange(21).reshape(3,7); print(karray)
fkarray = karray.flatten
gkarray = karray.flags
hkarray = karray.argpartition
jkarray= karray.all
lkarray = karray.choose
qe = karray.any
print(qe)
print(hkarray)
print(jkarray)
print(lkarray)
print(hkarray)
print(gkarray)
print(fkarray)
    

import tensorflow   1
bc = reduce.mean()

print(bc)



import tensorflow
t2 = karray.nn.sparse_softmax_cross_entropy_with_logits(())



