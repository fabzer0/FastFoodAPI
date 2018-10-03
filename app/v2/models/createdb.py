import os
import psycopg2
# from flask import current_app

def connect_to_db(config=None):
    """
    Function to connect to the required db
    """
    if config == 'testing':
        dbname = os.getenv('TEST_DB')
    else:
        dbname = os.getenv('MAIN_DB')

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')

    return psycopg2.connect(user=user, password=password, host=host, port=port, dbname=dbname)

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
            admin BOOLEAN DEFAULT FALSE,
            register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')

def create_meals_table(cur):
    cur.execute(
        '''CREATE TABLE meals (
            id serial PRIMARY KEY,
            mealname VARCHAR(50) NOT NULL UNIQUE,
            price INTEGER NOT NULL,
            in_menu BOOLEAN DEFAULT FALSE
        );''')

def create_orders_table(cur):
    cur.execute(
        '''CREATE TABLE orders (
            id serial,
            user_id INTEGER NOT NULL,
            ordername VARCHAR(50) NOT NULL,
            price INTEGER NOT NULL,
            status VARCHAR,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE
            );''')

def main(config=None):
    conn = connect_to_db(config=config)
    cur = conn.cursor()
    # cur.execute('DROP TABLE IF EXISTS users CASCADE')
    # cur.execute('DROP TABLE IF EXISTS meals CASCADE')
    # cur.execute('DROP TABLE IF EXISTS orders CASCADE')

    # create_users_table(cur)
    # create_meals_table(cur)
    # create_orders_table(cur)


    conn.commit()
    cur.close()
    conn.close()
    print('database successfully created')

if __name__ == '__main__':
    main()
