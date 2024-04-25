import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'phonebook',
    user = 'postgres',
    password = 'Araika06@'
    )

cur = conn.cursor()

# Delete table 
cur.execute('DROP TABLE phone_data')

conn.commit()

cur.execute("""CREATE TABLE phone_data(
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(255)
);""")

conn.commit()

# Create new numbers
cur.execute("""INSERT INTO phone_data (first_name, last_name, phone_number) VALUES 
            ('Ruslan', 'Khamitov', '+77007007070'),
            ('Mariya', 'Arystanova', '+77077077070'),
            ('Mansur', 'Ozatbekuly', '+77077070700'),
            ('Rasul', 'Zhumat', '+77077077077');
""")

conn.commit()

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