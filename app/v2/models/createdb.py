import os
import psycopg2

def connect_to_db(config=None):
    """
    Function to connect to the required db
    """

    return psycopg2.connect(os.getenv('DB_URL'))



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
            item VARCHAR(100) NOT NULL,
            totalprice INTEGER,
            status VARCHAR DEFAULT 'New',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE
            );''')

def main(config=None):
    conn = connect_to_db(config=config)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users CASCADE')
    cur.execute('DROP TABLE IF EXISTS meals CASCADE')
    cur.execute('DROP TABLE IF EXISTS orders CASCADE')

    create_users_table(cur)
    create_meals_table(cur)
    create_orders_table(cur)

    conn.commit()
    cur.close()
    conn.close()
    print('database successfully created')

