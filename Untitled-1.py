import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',name= 'root',psswd = '1234', database = 'world')
print('hello')