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
            name VARCHAR(255),
            phone_number VARCHAR(255)
);""")

conn.commit()

# Create new numbers
cur.execute("""INSERT INTO phone_data (name, phone_number) VALUES 
            ('Ruslan', '+77007007070'),
            ('Mariya', '+77077077070'),
            ('Mansur', '+77077070700'),
            ('Rasul', '+77077077077');
""")

conn.commit()

# Update phone_number
cur.execute("""UPDATE phone_data
            SET phone_number = '+77476737877'
            WHERE name = 'Mariya';
""")

conn.commit()

# Delete phone_number
cur.execute("""DELETE FROM phone_data
            WHERE phone_number = '+77007007070';
""")

conn.commit()