import sqlite3

DB_NAME = "patients.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        dob TEXT NOT NULL,
        email TEXT NOT NULL,
        glucose REAL NOT NULL,
        haemoglobin REAL NOT NULL,
        cholesterol REAL NOT NULL,
        risk_level TEXT,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_patient(
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        risk_level,
        remarks):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients(
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        risk_level,
        remarks
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        risk_level,
        remarks
    ))

    conn.commit()
    conn.close()


def get_all_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)
    )

    conn.commit()
    conn.close()