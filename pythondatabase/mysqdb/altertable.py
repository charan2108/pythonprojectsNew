import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="Stealth@foley2108", database="airbnb")

cur = myconn.cursor()

try:
    cur.execute("The alter  table is  add  EmployeeExpertise varchar(50) notnull")

except:  
    myconn.rollback()
    
myconn.close()      