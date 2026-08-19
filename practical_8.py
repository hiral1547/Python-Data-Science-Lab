# Aim : To write a Python program to connect with MySQL and perform basic 
# database operations such as INSERT, SELECT, UPDATE, and DELETE.

#==============================Theory===================================================
# MySQL is a relational database management system used to store data in tables.
# Python can communicate with MySQL using the MySQL Connector library.

# Basic SQL operations include:
#     CREATE TABLE — Creates a table.
#     INSERT — Adds records.
#     SELECT — Retrieves records.
#     UPDATE — Modifies existing records.
#     DELETE — Removes records.

# The mysql.connector module provides functions to establish a connection between 
# Python and MySQL.
# Note: Before running the program, install the connector using:

#     pip install mysql-connector-python

# Also replace the MySQL username and password in the program with your own credentials.

#========================================================================================

import mysql.connector

try:
    # Connect to MySQL
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

    cursor = con.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll_no INT PRIMARY KEY,
            name VARCHAR(50),
            marks INT
        )
    """)

    # Insert records
    students = [
        (101, "Rahul", 85),
        (102, "Priya", 90),
        (103, "Amit", 78)
    ]

    query = """
        INSERT IGNORE INTO student (roll_no, name, marks)
        VALUES (%s, %s, %s)
    """

    cursor.executemany(query, students)
    con.commit()

    # Display records
    print("Student Records:")
    cursor.execute("SELECT * FROM student")

    for row in cursor.fetchall():
        print(row)

    # Update record
    cursor.execute(
        "UPDATE student SET marks = %s WHERE roll_no = %s",
        (95, 101)
    )
    con.commit()

    print("\nAfter Update:")
    cursor.execute("SELECT * FROM student")

    for row in cursor.fetchall():
        print(row)

    # Delete record
    cursor.execute(
        "DELETE FROM student WHERE roll_no = %s",
        (103,)
    )
    con.commit()

    print("\nAfter Delete:")
    cursor.execute("SELECT * FROM student")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Database Error:", e)