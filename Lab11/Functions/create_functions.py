import psycopg2
from config import load_config


def create_function(sql_query):
    """ Create a function in the specified table """
    # sql query to create said function

    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                
                # create a function for the specified table
                cur.execute(sql_query)
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    query1 = """
            CREATE OR REPLACE FUNCTION phone_book(id INTEGER)
            RETURNS TABLE(first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT parts.first_name, parts.last_name, parts.phone_number
            FROM parts;

            END; $$

            LANGUAGE plpgsql;
            """
    
    query2 = """
            CREATE OR REPLACE FUNCTION phone_book()
            RETURNS TABLE(first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT * FROM phone_data;

            END; $$

            LANGUAGE plpgsql;
            """

    create_function(query2)