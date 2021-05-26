import cx_Oracle
try:
    con =cx_Oracle.connect("system/root@localhost")
    cursor =con.cursor()
    cursor.execute("create table emp(emp id, emp name varchar2(10),empsal number(10,2),empaddress varchar2(10))")
    print("Table created successfully")
except cx_Oracle.databaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
      cursor.close()
    if con:
        con.close() 
                       
    