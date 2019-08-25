from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error
import os
import sqlalchemy
import pymysql

string = ''
string2 = ''

try:
    connection = mysql.connector.connect(host=os.environ.get('thehost'),
                             database=os.environ.get('thedatabase'),
                              user=os.environ.get('theuser'),
                             password=os.environ.get('thepassword'))
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ",db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print ("Your connected to - ", record)
        
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM groceries WHERE id = 1")
        string = mycursor.fetchall()
        

except Error as e :
    print ("Error while connecting to MySQL", e)


finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

"""
engine = sqlalchemy.create_engine(os.environ.get('omega'))


rs = engine.connect().execute('SELECT * FROM groceries WHERE id = 2')
for row in rs:
    string2 += str(row)

"""

app = Flask(__name__)

@app.route('/')
def hello_world():
    return string