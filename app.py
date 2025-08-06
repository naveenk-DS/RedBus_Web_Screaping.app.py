import mysql.connector
import pandas as pd

def load_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    query = "SELECT * FROM bus_details"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
