import psycopg2
from config import load_config


def add_phone_number(fname, lname, number):
    """ Add a new phone_number """
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute('CALL new_number(%s,%s, %s)', (fname, lname, number))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    insert = add_phone_number('Arai', 'Zhumat', '+77236737856')
    print(insert)