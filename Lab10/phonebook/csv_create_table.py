import psycopg2

#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'phonebook',
    user = 'postgres',
    password = 'Araika06@'
    )

#Create a cursor to work with the database
cur = conn.cursor()

# Delete table 
cur.execute('DROP TABLE phone_data')

conn.commit()

# Create a new table
cur.execute("""CREATE TABLE phone_data(
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(255)
);""")

conn.commit()

import csv

filename = 'PhoneBook.csv'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        first_name, last_name, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phone_data (first_name, last_name, phone_number) VALUES
            ('{first_name}', '{last_name}','{phone_number}');
            """)
        
        conn.commit()
        
        cur.execute('SELECT * FROM phone_data;')

        cur.execute('SELECT * FROM phone_data ORDER BY first_name asc;')
        
        print(cur.fetchone())
        
        # Update phone_number
        cur.execute("""UPDATE phone_data
            SET phone_number = '+77476737877'
            WHERE first_name = 'Mariya';
            """)
        conn.commit()
        
        # Delete phone_number
        cur.execute("""DELETE FROM phone_data
            WHERE phone_number = '+77007007070';
            """)
        
        conn.commit()