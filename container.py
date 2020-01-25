# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:49:58 2019

@author: ojhas

List
Tuple
Dictionary
Arrays
Set and Frozenset


List: store and manipulate data stored in sequential order. (Mutable Object)
      list()
      [ ]
      Homogeneous/Hetrogeneous data can be stored

"""

list1 = [100, 'sanjiv', 45.455, "sanjiv@gmail.com"]
print (list1[0:2] )

#For loop
for data in list1:
    print (data)
    
# List to maintain employee salary detail
salary=[1232,435,66767,23232,22344]
print (salary)
#builtin sum,max,min
print ("Sum: ",sum(salary))
print ("MAx: ",max(salary))
print ("Min: ",min(salary))
print ("Average: ",sum(salary)/len(salary))

"""
#List Operations
    Inserting
    Appending
    Removing
    indexing
    Slicing    
"""

scores=[23,45,66,78,33,45,77]
print (scores)
scores.insert(0,44)
print (scores)
scores.append(99)
print (scores)
scores.remove(33)
print (scores)

indexno = int(input("Enter idx:"))
print (scores[indexno])
scores[indexno]=int(input("Enter a anew value:"))
print (scores)

print (list(filter(lambda x: x==66, scores)))

"""
List exercises

Code to create list of names, and find the given name presetnt or not 


"""

names = []
while(True):
    nm = input("Enter name:")
    if (len(nm) > 0):
        names.append(nm)
    else:
        break

print (names)

while(True):
    nm = input("Enter name to find:")
    if (len(nm) == 0 ):
        break
    if ( nm in names):
        print ("{} found in the list".format(nm))
    else:
        print ("Not Found")







"""
Code to find the grades based in students scores 
"""
marks = []
while(True):
    s=int(input("Enter marks(enter -1 to stop):"))
    if (s==-1):
        break
    marks.append(s)

print (marks)

def markstograde(m):
    if (m < 35):
        return "Failed"
    elif (m>=35 and m<60):
        return "B grade"
    elif (m>=60 and m<75):
        return "A grade"
    elif m>=75:
        return "Excellent"


grades=list(map(lambda x: markstograde(x), marks ))

reduce    
#grades = []
#for i in marks:
#   grades.append(markstograde(i))

marks.sort()
import matplotlib.pyplot as pt

pt.plot(marks)
pt.bar(grades, marks)
pt.show()






































