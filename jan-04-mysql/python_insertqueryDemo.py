import mysql.connector
from mysql.connector import connect

#first i am connecting to the mysql database server
connection = mysql.connector.connect(host='localhost',
                             database='proj1',
                             user='root',
                             password='')
#opening the cursor
cursor = connection.cursor()  #create cursor object to execute the sql queryies from python code
#set the query
idno=int(input("enter the Idno"))
name=input("enter the name")
insertquery="insert into simple123 values('%s','%s')"%(idno,name)
#execute the queries
cursor.execute(insertquery)
connection.commit() #to save the changes in the database table.
cursor.close()
connection.close()
        
