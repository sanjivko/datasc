import mysql.connector
from mysql.connector import connect

#first i am connecting to the mysql database server
connection = mysql.connector.connect(host='localhost',database='proj1',user='root',password='')
#opening the cursor
cursor = connection.cursor()
cursor.execute("select *from simple123")
record = cursor.fetchall()
print ("Your connected to - ", record)
#rows wise accessing data
for data in record:
     print(data)
cursor.close()
connection.close()
        
