import os
import psycopg2


def connect_to_db(config=None):
    """
    Function to connect to the required db
    """

    if config == 'testing':
        db_name = os.getenv('TEST_DB')
    else:
        db_name = os.getenv('DB_NAME')

    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PWD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    return psycopg2.connect(user=user, password=password, host=host, port=port, database=db_name)

def create_users_table(cur):
    """
    Functions to create table for users
    """
    cur.execute(
        '''CREATE TABLE users (
            id serial PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')


def create_menu_table(cur):
    cur.execute(
        '''CREATE TABLE menu (
            id serial PRIMARY KEY,
            menu_item VARCHAR(50) NOT NULL UNIQUE,
            price INTEGER NOT NULL,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')

def create_orders_table(cur):
    cur.execute(
        '''CREATE TABLE orders (
            id serial,
            ordername VARCHAR(50) NOT NULL,
            price INTEGER NOT NULL,
            status VARCHAR,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );''')



def main(config=None):
    conn = connect_to_db(config=config)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users CASCADE')
    cur.execute('DROP TABLE IF EXISTS menu CASCADE')
    cur.execute('DROP TABLE IF EXISTS orders CASCADE')

    create_users_table(cur)
    create_menu_table(cur)
    create_orders_table(cur)


    conn.commit()
    cur.close()
    conn.close()
    print('database successfully created')


if __name__ == '__main__':
    main()
