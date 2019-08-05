from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error
import os
string = ''
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
app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(string)