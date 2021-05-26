import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="Stealth@mode2108", database="airbnb")

cur = myconn.cursor()

try:
    cur.execute("create table Employee(name varchar(255) not null, id int(255) not null primary key, dept varchar(255) not null )")
    

except:
    myconn.rollback()
    
myconn.close()        