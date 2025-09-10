# database/db_connection.py

import mysql.connector
from config.db_config import DB_CONFIG

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("✅ Connection successful!")
            return conn
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None
