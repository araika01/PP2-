import psycopg2

#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'suppliers',
    user = 'postgres',
    password = 'Araika06@'
    )

#Create a cursor to work with the database
cur = conn.cursor()

# Querying the database
cur.execute('SELECT Version()')

db_ver = cur.fetchall()

print(db_ver)