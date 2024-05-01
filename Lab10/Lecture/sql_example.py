#SQL

# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

import psycopg2

#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'students',
    user = 'postgres',
    password = 'Araika06@'
    )

#Create a cursor to work with the database
cur = conn.cursor()

# Delete table 
cur.execute('DROP TABLE students_data')

conn.commit()

# Create a new table
cur.execute("""CREATE TABLE students_data(
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            study_year INT,
            phone_number VARCHAR(20)
);""")

conn.commit()

# Create new students
cur.execute("""INSERT INTO students_data (name, id, study_year, phone_number) VALUES
            ('Ruslan', '24B202424', 1, '+77007007070'),
            ('Mariya', '24B202425', 1, '+77077077070');
""")

conn.commit()

# Get students
cur.execute('SELECT name, id, phone_number, study_year FROM students_data')

print(cur.fetchall())
print(cur.fetchall())

cur.execute('SELECT name, id, phone_number, study_year FROM students_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())


# Update students
cur.execute("""UPDATE students_data
            SET study_year = 2
            WHERE id = '24B202424';
""")

conn.commit()

# Delete students
cur.execute("""DELETE FROM students_data
            WHERE id = '24B202424';
""")

conn.commit()