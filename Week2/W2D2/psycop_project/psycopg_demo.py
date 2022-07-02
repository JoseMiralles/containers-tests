from typing import Dict
import psycopg2

CONNECTION_PARAMETERS = {
    'dbname': 'psycopg_test_db',
    'user': 'psycopg_test_user',
    'password': 'password',
    'host': 'localhost',
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM "cars"')
        cars = curs.fetchall()
        for car in cars:
            print(car)
