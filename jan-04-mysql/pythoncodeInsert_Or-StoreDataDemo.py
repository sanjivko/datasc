#python code to store data within the database tables
import mysql.connector
from mysql.connector import connect

#first i am connecting to the mysql database server
connection = mysql.connector.connect(host='localhost',
                             database='db123',
                             user='root',
                             password='')
#opening the cursor
cursor = connection.cursor()  #create cursor object to execute the sql queryies from python code

#set the insert query
idno=int(input("enter the idno"))
name=input("enter the name")

ins_query="insert into simple123 values('%s','%s')"%(idno,name)

print(ins_query)
cursor.execute(ins_query)

connection.commit() #connection commit stores data within the database
connection.close()



