import mysql.connector
from mysql.connector import connect

#first i am connecting to the mysql database server
connection = mysql.connector.connect(host='localhost',
                             database='proj1',
                             user='root',
                             password='')
#opening the cursor
cursor = connection.cursor()  #create cursor object to execute the sql queryies from python code
#execute the queries
cursor.execute("create table simple123(id int,name char(20))")
cursor.close()
connection.close()
        
