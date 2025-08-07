import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Naveen@677',  # Replace with your MySQL password
        database='redbus_data'
    )
