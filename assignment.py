# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:39:22 2019

Create a database in the following format

Values	=	Router1		1.1.1.1	 	zframez		zframez
Keys	=	(name)		(IP)		(username)	(pwd)

1. Write a python program to print the value of a given key

2. Write a python program to check whether the given key is present, 
   if present print the value , else add a new key and value
"""
db = {
       "name" : "Router1",
       "ip" : "1.1.1.1",
       "username": "abc",
       "pwd": "pass"
       }
k = input("Enter key to find:")
if  k in list(db.keys()): 
    print(db[k])
else:
    val = input("Key not found, enter value to add:")      
    db[k]=val
    print(db)



"""
Create a database in the following format

	Interface		IP			status
	
1	Ethernet0		1.1.1.1			up
2	Ethernet1		2.2.2.2			down
3	Serial0		    3.3.3.3			up
4	Serial1		    4.4.4.4			up

3. Write a python program to find status of a given interface

4. Write a python program to find interface and IP of all interfaces which are up

5. Write a python program to count how many ethernet interfaces are there

6. Write a python program to add a new entry to above database
"""

db2 = [{
            "interface" : "eth0",
            "ip" : "1.1.1.1",
            "status" : "up"
        },
        {
            "interface" : "eth1",
            "ip" : "2.2.2.2",
            "status" : "down"
            },
        {
            "interface" : "ser0",
            "ip" : "3.3.3.3",
            "status" : "up"
        },
        {
            "interface" : "ser1",
            "ip" : "4.4.4.4",
            "status" : "up"
        }    
       ]

print ("Check Status ")
print ("===============")

iface=input("Enter interface:")
for e in db2:    
    if e["interface"] == iface:
        print ( "Status of ", e["interface"] ,"is", e["status"])


print ("find interface and IP of all interfaces which are up")
print ("=====================================================")
for e in db2:    
    if e["status"] == "up":
        print ( "Status of ", e["interface"] ,"is", e["status"])
        
print ("Write a python program to count how many ethernet interfaces are there")
print ("=====================================================")
import re
count = 0
for e in db2:    
    if (re.search("eth",e["interface"]) != None):
        count += 1;
print ("Ethernet interface count:",count)


print ("Write a python program to add a new entry to above database")
print ("=====================================================")

print ("Enter new interface details:")

tmp={}
d=input("Enter iface name:")
tmp["interface"]=d
d=input("Enter ip address:")
tmp["ip"]=d
d=input("Enter interface status:")
tmp["status"]=d

db2.append(tmp)

print (db2)



