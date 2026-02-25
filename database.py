import sqlite3

DB_NAME = "practice.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def setup_database():
    conn = get_connection()
    cur = conn.cursor()

    # Employees table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER,
        join_date TEXT
    )
    """)

    # Departments table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT
    )
    """)

    # Reset data
    cur.execute("DELETE FROM employees")
    cur.execute("DELETE FROM departments")

    employees = [
        (1, "Amit", "IT", 70000, "2020-01-10"),
        (2, "Neha", "HR", 50000, "2019-03-15"),
        (3, "Ravi", "IT", 80000, "2021-07-20"),
        (4, "Anjali", "Finance", 60000, "2018-11-25"),
        (5, "Rahul", "IT", 90000, "2022-02-01"),
        (6, "Kiran", "HR", 45000, "2020-06-12"),
        (7, "Suman", "Finance", 75000, "2021-08-18")
    ]

    departments = [
        (1, "IT"),
        (2, "HR"),
        (3, "Finance")
    ]

    cur.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees)
    cur.executemany("INSERT INTO departments VALUES (?, ?)", departments)

    conn.commit()
    conn.close()
