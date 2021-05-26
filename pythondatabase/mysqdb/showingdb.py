# import connector
import mysql.connector

# creating the connection 
myconn = mysql.connector.connect(host="localhost", user="root", password="Stealth@mode2108")

# creating cursor
cur = myconn.cursor()

try:
    dbs=cur.execute("show databases")

except:
    myconn.rollback()    

for x in cur:
    print(x)
    
myconn.close()        