import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",passwd="0000")

cursor = mydb.cursor()
#cursor.execute("show databases")
cursor.execute("create database if not exists iNeuron")
cursor.execute("use iNeuron")
cursor.execute("create table if not exists iNeuron.table1(emp_id int(10), name varchar(20), address varchar(30))")
#cursor.execute("insert into table1 values(101,'Yash Vij','Noida, UP')")
##cursor.execute("insert into table1 values(102,'Yash Vij','Noida, UP')")
#cursor.execute("insert into table1 values(103,'Yash Vij','Noida, UP')")
#cursor.execute("insert into table1 values(104,'Yash Vij','Noida, UP')")
mydb.commit()
#cursor.execute("delete from table1 where emp_id = 103")

cursor.execute("Select * from table1")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)