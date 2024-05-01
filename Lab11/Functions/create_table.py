import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'phonebook',
    user = 'postgres',
    password = 'Araika06@'
    )

cur = conn.cursor()


cur.execute("""CREATE TABLE phone_data(
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(255)
);""")

conn.commit()
