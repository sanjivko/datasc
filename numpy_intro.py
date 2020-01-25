# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 09:06:38 2020

@author: ojhas

numpy intro

"""


[x for x in range(0,10)]
list(range(10))
[x for x in range(0,9) if x%2 != 0]

import numpy as np
np.__version__
help(np)


ar = np.array([[12,  7,  5,  5],
      [ 0,  1,  5,  9],
      [ 3,  0,  5,  0]])


np.histogram(ar)

my_3d_array = np.array([[[1,2,3,4], [5,6,7,8]], [[1,2,3,4], [9,10,11,12]]], dtype=np.int64)
import matplotlib.pyplot as plt
plt.hist(my_3d_array.ravel(), bins=range(0,13))
plt.title('Frequency of My 3D Array Elements')
plt.show()


np.arange(.1, dtype=float)

np.linspace(1,10,10, dtype=np.int64)
np.indices((3,3))

np.zeros((2,3), dtype=np.int64)

#identity matrix
np.eye(3)


np.random.normal(0, 10, 20)

import matplotlib.pyplot as plt
import seaborn as sn
sn.lineplot(np.arange(20), np.random.normal(0,10,20))
plt.(np.random.normal(0,10,20))


np.random.seed(0)
arr = np.random.normal(0,10,(4,4))
type(arr)
arr.ndim

arr
arr[::2]
arr[::2, ::2]




np.concatenate([np.random.normal(1,20, (2,2)), np.random.normal(1,20, (2,2))])

arr1 = np.random.normal(1,20, (2,2))

np.vstack([arr1, np.arange(2)])
np.hstack([arr1, np.arange(2)])

np.arange(10).max()

help(np.concatenate)


'''
split 
'''



x = np.arange(0,6*np.pi,.1)
y = np.sin(x)
plt.autoscale(enable=True)
plt.title("Quad fun")
plt.xlabel("x label")
plt.ylabel("y label")
plt.plot(x,y, color='green')
plt.show()





x = np.arange(0,6*np.pi,.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y_sin, color='green')
plt.plot(x, np.full((len(x),), 0))

plt.subplot(2,1,2)
plt.plot(x,y_cos, color='red')
plt.plot(x, np.full((len(x),), 0))

from sklearn.datasets import load_iris
iris_ds = load_iris()
plt.plot(iris_ds.data)
plt.plot(np.array(iris_ds.data)[:,0:3])


plt.bar(iris_ds.data[:,0:1], iris_ds.data[:,2:3],width=.5)

plt.bar(range(len(iris_ds.data)), iris_ds.data[:,2:3], width=.1)

plt.hist(iris_ds.data[:,0:1], bins=np.arange(0,15,.4))






