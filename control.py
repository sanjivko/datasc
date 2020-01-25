# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 08:49:36 2019

@author: ojhas
"""

"""
CONTROL Structures
Conditional
   if else elif  
   
Iterative

"""

score = int(input("Enter Score:"))
if score < 35:
    print ("Failed")
else:
    print ("Passed")



n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
#print(max(n1,n2))
if (n1 < n2):
    print("{} is bigger".format(n2))
elif(n1 > n2):
    print("{} is bigger".format(n1))
else:
    print("{} {} are same".format(n1,n2))    


#Neg pos check
n2 = int(input("Enter n2:"))
if (n2>0):
    print ("Positive")
elif (n2<0):
    print ("Negative")
else:
    print ("Zero")




#odd even
n2 = int(input("Enter n2:"))
if (n2%2==0):
    print ("Even")
elif (n2%2 != 0):
    print ("Odd")


"""
Nested if
"""
username=input("Username:")
if(username == "admin"):
    paswd = input("Password:")
    if(paswd == "pass"):
        print ("Login success")
    else:
        print ("Invalid passwd")
else:
    print ("Invalid user")



marks = float(input("Enter marks:"))
if (marks >=35 and marks <60):
    print ("B grade")
elif (marks >=60 and marks < 75):
    print ("A Grade")
elif (marks >=75 and marks<=100):
    print ("Distinction")
else:
    print ("Failed")


#Age and validate minor major, senior
age=int(input("Enter age:"))
if (age<18):
    print ("MINOR")
elif (age>=18 and age <60):
    print ("MAJOR")
elif (age >=60):
    print ("Senior")
    
    
    
    

"""

Iterative control or Looping

for loop
while loop

"""

print ([x for x in range(1,10,2)])

"""
Using for loops for string
"""

name = "Hello World"

import re
text=input("Enter string:")
print ([i for i in text if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'])

print ([i for i in text if re.search(i,"aeiou")])


i=0
while  i<10:
    print (i)
    i += 2































