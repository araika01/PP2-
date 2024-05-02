import psycopg2
from config import load_config

def create_proc():
    """ Create procedures in the PostgreSQL database"""
    commands = (
        """
        CREATE OR REPLACE PROCEDURE new_number(
           fname varchar,
           lname varchar,
           number varchar
        )
        AS $$
        BEGIN
            UPDATE phone_data
            SET phone_number = number
            WHERE first_name = fname and last_name = lname;
        
            IF NOT FOUND THEN 
            INSERT INTO phone_data(first_name, last_name, phone_number)
            VALUES(fname, lname, number);s
            END IF;
        END;
        $$
        LANGUAGE PLPGSQL;      
        """,
        )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_proc()