import sqlite3
import pandas as pd

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT NOT NULL,
        student_education TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tutors (
        tutor_id INTEGER PRIMARY KEY,
        tutor_name TEXT NOT NULL,
        tutor_expertise TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS memberships (
        membership_id INTEGER PRIMARY KEY,
        membership_type TEXT NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (student_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contracts (
        contract_id INTEGER PRIMARY KEY,
        base_salary INTEGER NOT NULL,
        bonus INTEGER NOT NULL,
        tutor_id INTEGER NOT NULL,
        FOREIGN KEY (tutor_id) REFERENCES tutors (tutor_id)
    )
''')

conn.commit()
conn.close()

print('Tabelas criadas com sucesso!')