from sqlite3 import connect
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mynewdatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)