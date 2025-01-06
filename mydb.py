# install mysql on local machine
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='abinroy'
    
)
#cursor object
cursorObject =dataBase.cursor()

#database
cursorObject.execute("CREATE DATABASE abinco")
print("All Done!")