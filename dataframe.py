import sqlite3
import pandas as pd
from IPython.display import display


# Conectar ao banco de dados
conn = sqlite3.connect('escola.db')

# --- Carregar e exibir tabelas completas ---
try:
    students_df = pd.read_sql('SELECT * FROM students', conn)
    print("Tabela Students:")
    display(students_df)

    tutors_df = pd.read_sql('SELECT * FROM tutors', conn)
    print("\nTabela Tutors:")
    display(tutors_df)

    # --- INNER JOIN 1: Students e Memberships ---
    inner_join_1 = pd.read_sql('''
        SELECT students.student_name, memberships.membership_type
        FROM students
        INNER JOIN memberships ON students.student_id = memberships.student_id
    ''', conn)
    print("\nINNER JOIN - Students e Memberships:")
    display(inner_join_1)

    # --- INNER JOIN 2: Tutors e Contracts ---
    inner_join_2 = pd.read_sql('''
        SELECT tutors.tutor_name, contracts.base_salary, contracts.bonus
        FROM tutors
        INNER JOIN contracts ON tutors.tutor_id = contracts.tutor_id
    ''', conn)
    print("\nINNER JOIN - Tutors e Contracts:")
    display(inner_join_2)

    # --- SELECT 1: Alunos de Engenharia ---
    select_1 = pd.read_sql('SELECT student_name FROM students WHERE student_education = "Engenharia"', conn)
    print("\nSELECT - Alunos de Engenharia:")
    display(select_1)

    # --- SELECT 2: Tutors de História ---
    select_2 = pd.read_sql('SELECT tutor_name FROM tutors WHERE tutor_expertise = "História"', conn)
    print("\nSELECT - Tutors de História:")
    display(select_2)

except Exception as e:
    print("Erro ao executar consultas:", e)

finally:
    conn.close()
    print('\nConsultas finalizadas! ✅')