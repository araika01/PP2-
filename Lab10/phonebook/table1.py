import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'phonebook',
    user = 'postgres',
    password = 'Araika06@'
    )

cur = conn.cursor()

"""# Delete table 
cur.execute('DROP TABLE phone_data')

conn.commit()


# Create a new table
cur.execute("""CREATE TABLE phone_data(
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(255)
);""")"""

conn.commit()

first_name = input()
last_name = input()
phone_number = input()

cur.execute("INSERT INTO phone_data (first_name, last_name, phone_number) VALUES(%s, %s, %s)",
            (first_name, last_name, phone_number))

conn.commit()