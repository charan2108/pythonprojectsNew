# import 
import mysql.connector

# creating the connector
myconn = mysql.connector.connect(host="localhost", user="root", password="Stealth@mode2108" )

# creating the cursor
cur = myconn.cursor()

try:
    # create new database
    cur.execute("create database AirBnb")
    
    dbs = cur.execute("show databases")
    
except:
    myconn.rollback()
    
for x in cur:
    print(x)
    
myconn.close()            
