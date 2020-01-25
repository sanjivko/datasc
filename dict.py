# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:01:17 2019

@author: ojhas

dictionary
array
set & frozenset
"""

import requests as req
import pprint as pp

book = {
         "id": 1,
         "name": "Test Book",
         "price": 450
        }

print (book)

print (",".join((list(book.keys()))))


for i in book.values():
    print (i)
    

for k,v in book.items():
    print (k,":", v)
    
    

res=req.get("https://reqres.in/api/users?page=1")
d = res.json()


"""
Nested Dictionary

"""
org = {
        "HR":{"Dept no": "D1",
             "Manager": "Dk",
             "loc" : "BlocA",
             "Ext" : "1232",
             "TeamSize": 5
               },
        "ADMIN":{"Dept no": "D2",
             "Manager": "Dk",
             "loc" : "BlocA",
             "Ext" : "1232",
             "TeamSize": 20
            },
        "TECH ENGG":{"Dept no": "D3",
             "Manager": "Dk",
             "loc" : "BlocA",
             "Ext" : "1232",
             "TeamSize": 15
                    }
        }
            
            
print (org)

x=list(org.keys())
y=[]
for i in x:
    y.append(org[i]["TeamSize"])
print(y)


import matplotlib.pyplot as pt
pt.bar(x,y)





"""
Array module.

array typecodes
i integer
f float
u char
"""
import array as ar

ar.array("i", [1,23,45])

"""
File Operations

A file is a collection of various records grouped together

It can be of any type
   . csv files
   . txt files
   . bin files
   . json files
   . xml/html 
   
   
   w - write
   r - read
   r+ - readwrite
   wb/rb - rw binary mode
   
"""


import sklearn
from sklearn import *

print (sklearn.datasets.load_diabetes())


d  = sklearn.datasets.load_diabetes()

list(d.keys())




employees = {
        "idno":{
                "1": 100,
                "2": 101,
                "3": 103
                },
        "names":{
                "1": "sdf",
                "2": "dfff",
                "3": "bbb"

                }
        
        }

f1=open("emp.csv", "w")

f1.write(",".join(employees.keys()))
f1.write("\n")
for i in employees["idno"].keys():
    f1.write( str(employees["idno"][i])+','+employees["names"][i])
    f1.write("\n")
    
f1.close()



"""

Python read csv files

"""


f2=open("emp.csv", "r")
print (f2.read().split("\n"))
f2.seek(0)
print (f2.read())





























