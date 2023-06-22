import mysql.connector
from mysql.connector import Error

def create_connection(DB_HOST, DB_USER, DB_PASS):
    connection = None
    try:
      connection = mysql.connector.connect(
          host= DB_HOST,
          user= DB_USER,
          passwd= DB_PASS
      )
      print("Connection to MySQL DB successful")
    except Error as e:
      print(f"The error '{e}' occurred")
    return connection

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
