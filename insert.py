import sqlite3
import pandas as pd

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO students (student_name, student_education) VALUES ('Carlos', 'Engenharia')")
cursor.execute("INSERT INTO students (student_name, student_education) VALUES ('Mariana', 'Medicina')")

cursor.execute("INSERT INTO tutors (tutor_name, tutor_expertise) VALUES ('João', 'Matemática')")
cursor.execute("INSERT INTO tutors (tutor_name, tutor_expertise) VALUES ('Ana', 'História')")

cursor.execute("INSERT INTO memberships (membership_type, student_id) VALUES ('Gold', 1)")
cursor.execute("INSERT INTO memberships (membership_type, student_id) VALUES ('Silver', 2)")

cursor.execute("INSERT INTO contracts (base_salary, bonus, tutor_id) VALUES (3000, 500, 1)")
cursor.execute("INSERT INTO contracts (base_salary, bonus, tutor_id) VALUES (2500, 400, 2)")

conn.commit()
conn.close()

print('Dados inseridos com sucesso!')