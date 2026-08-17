from database import create_connection


# Insert sample data into the database
def insert_sample_data():
    conn = create_connection()
    cursor = conn.cursor()
    # ---------------- Students ----------------
    if not record_exists(cursor, "Student", "student_id", 1):
        cursor.execute("""
        INSERT INTO Student
        VALUES (1, 'Richard', 'Xiahou', '1995-01-01')
        """)
    if not record_exists(cursor, "Student", "student_id", 2):
        cursor.execute("""
        INSERT INTO Student
        VALUES (2, 'Tom', 'Smith', '1998-05-10')
        """)

    if not record_exists(cursor, "Student", "student_id", 3):
        cursor.execute("""
        INSERT INTO Student
        VALUES (3, 'Amy', 'Wilson', '1999-03-18')
        """)

    if not record_exists(cursor, "Student", "student_id", 4):
        cursor.execute("""
        INSERT INTO Student
         VALUES (4, 'Jack', 'Brown', '1997-11-20')
        """)

    if not record_exists(cursor, "Student", "student_id", 5):
        cursor.execute("""
            INSERT INTO Student
            VALUES (5, 'Lucy', 'Taylor', '2000-07-15')
        """)

    # ---------------- Lecturers ----------------

    if not record_exists(cursor, "Lecturer", "lecturer_id", 1):
        cursor.execute("""
        INSERT INTO Lecturer
        VALUES (1, 'John', 'Miller', 'john@college.ac.nz')
        """)

    if not record_exists(cursor, "Lecturer", "lecturer_id", 2):
        cursor.execute("""
        INSERT INTO Lecturer
        VALUES (2, 'Sarah', 'Lee', 'sarah@college.ac.nz')
        """)

    # ---------------- Subjects ----------------

    if not record_exists(cursor, "Subject", "subject_id", 1):
        cursor.execute("""
        INSERT INTO Subject
        VALUES (1, 'Python Programming', 15, 1)
        """)
    
    if not record_exists(cursor, "Subject", "subject_id", 2):
        cursor.execute("""
        INSERT INTO Subject
        VALUES (2, 'Database Systems', 15, 2)
        """)
    
    if not record_exists(cursor, "Subject", "subject_id", 3):
        cursor.execute("""
        INSERT INTO Subject
        VALUES (3, 'Software Engineering', 15, 1)
        """)

    # ---------------- Enrollments ----------------

    if not record_exists(cursor, "Enrollment", "enrollment_id", 1): 
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (1, 1, 1, '2026-08-01')
        """)
    
    if not record_exists(cursor, "Enrollment", "enrollment_id", 2):
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (2, 1, 2, '2026-08-01')
        """)

    if not record_exists(cursor, "Enrollment", "enrollment_id", 3):
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (3, 2, 1, '2026-08-02')
        """)

    if not record_exists(cursor, "Enrollment", "enrollment_id", 4):
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (4, 3, 2, '2026-08-02')
        """)

    if not record_exists(cursor, "Enrollment", "enrollment_id", 5):
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (5, 3, 3, '2026-08-03')
        """)

    if not record_exists(cursor, "Enrollment", "enrollment_id", 6):
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (6, 4, 3, '2026-08-03')
        """)
   
    if not record_exists(cursor, "Enrollment", "enrollment_id", 7):
        cursor.execute("""
        INSERT INTO Enrollment
        VALUES (7, 5, 1, '2026-08-04')
        """)
    conn.commit()
    conn.close()
    print("Sample data inserted successfully.")

#  Check if a record exists，
def record_exists(cursor, table_name, id_name, id_value):
    sql = f"SELECT * FROM {table_name} WHERE {id_name} = ?"
    cursor.execute(sql, (id_value,))

    result = cursor.fetchone()
    if result:
        return True
    return False
# Show how many students are registered in each subject
def show_student_count():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        Subject.subject_name,
        COUNT(Enrollment.student_id)
    FROM Subject
    JOIN Enrollment
        ON Subject.subject_id = Enrollment.subject_id
    GROUP BY Subject.subject_name
    """)

    results = cursor.fetchall()
    print("\nStudent count in each subject")
    for row in results:
        print(row[0], ":", row[1])
    conn.close()
# Show students who enrolled in more than one subject
def show_students_more_than_one_course():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        Student.student_id,
        Student.first_name,
        Student.last_name,
        COUNT(Enrollment.subject_id)
    FROM Student
    JOIN Enrollment
        ON Student.student_id = Enrollment.student_id
    GROUP BY Student.student_id
    HAVING COUNT(Enrollment.subject_id) > 1
    """)
    results = cursor.fetchall()
    print("\nStudents enrolled in more than one subject")
    for row in results:
        print(
            row[0],
            row[1],
            row[2],
            "-",
            row[3],
            "subjects"
        )
    conn.close()

def show_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    results = cursor.fetchall()
    print("\nStudent List")
    for row in results:
        print(row)
    conn.close()