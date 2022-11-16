import pandas as pd
import pymysql
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="0000")

cursor = mydb.cursor()
# cursor.execute("show databases")
cursor.execute("create database if not exists iNeuron")
cursor.execute("use iNeuron")
df = pd.read_csv("bank/bank.csv",sep = ";")
print(df.columns)
cols = "`,`".join([str(i) for i in df.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in df.iterrows():
    sql = "INSERT INTO bank_details (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    mydb.commit()
mydb.close()