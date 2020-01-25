# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 08:57:39 2019

@author: ojhas
"""

"""

"""


n = range(0,10)


even = filter(lambda x:x%2==0, n)
print ([i for i in even])



"""
reduce()
returns single value as an output from the collection of values

"""

import functools
from functools import reduce
help(reduce)


reduce (lambda x,y: x+y*y, range(0,10))


def max1(x,y):
    if x>y:
        return x
    return y

reduce (lambda x,y: max1(x,y), range(0,10))

reduce (lambda x,y: x if x > y else y, range(0,10))

reduce (lambda x,y: x if x < y else y, range(0,10))



"""
module is a reusable file
module is collection of functions,  variables, classes

- Biltin modules
- user defined
"""

import mathsoper







