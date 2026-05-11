'''This is a SQL DATa base made by sohail'''

#This bit of code is to connect my SQl data base to python
import sqlite3
db = sqlite3.connect("3DPRINTER.DB")
cursor = db.cursor()

#this is a Query test
sql = "SELECT * FROM PRINTER_3D;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close