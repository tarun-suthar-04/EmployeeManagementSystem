# database/db_connection.py
import mysql.connector
from config.db_config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def AddEmployee(Id, Name, Salary):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Employee (Id, Name, Salary) VALUES (%s, %s, %s)"
    values = (Id, Name, Salary)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def UpdateEmployee(Id, Name, Salary):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Employee SET Name = %s, Salary = %s WHERE Id = %s"
    values = (Name, Salary, Id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def DeleteEmployee(Id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Employee WHERE Id = %s"
    values = (Id,)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def FetchRecords():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

if __name__ == "__main__":
    # import menu and run
    from ui.menu import run_menu
    run_menu()
