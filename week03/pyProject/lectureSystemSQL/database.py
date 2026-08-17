import sqlite3


# Create a connection to the database
def create_connection():
    conn = sqlite3.connect("lectureSystem.db")
    return conn

# Create all tables
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # ---------------- Student ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student(
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        birth_date TEXT
    )
    """)

    # ---------------- Lecturer ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Lecturer(
        lecturer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
    """)

    # ---------------- Subject ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subject(
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT,
        subject_unit INTEGER,
        lecturer_id INTEGER
    )
    """)

    # ---------------- Enrollment ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollment(
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        enroll_date TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("Database created successfully.")