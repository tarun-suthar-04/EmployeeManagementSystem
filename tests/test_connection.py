# ui/test_connection.py

from database.db_connection import get_connection
#
# conn = get_connection()
# if conn:
#     conn.close()
# from database.db_connection import get_connection


def create_employee_table():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE Employee (
    Id INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL
);

        """)

        conn.commit()
        print("✅ Employee table created successfully!")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    create_employee_table()
