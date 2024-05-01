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


