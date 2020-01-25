# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:53:45 2020

@author: ojhas
"""
import mysql
import mysql.connector
from mysql.connector import connect

#first i am connecting to the mysql database server
connection = mysql.connector.connect(host='192.168.56.4',                             
                             user='root',
                             database="test"
                             
                             )

cursor = connection.cursor()  #create cursor object to execute the sql queryies from python code
#set the query
idno=int(input("enter the Idno"))
name=input("enter the name")
age=int(input("Enter age:"))
insertquery="insert into students values('%s','%s',%d)"%(idno,name,age)
#execute the queries
cursor.execute(insertquery)
connection.commit() #to save the changes in the database table.


cursor.execute("select * from students")

records =cursor.fetchall()



cursor.close()
connection.close()




