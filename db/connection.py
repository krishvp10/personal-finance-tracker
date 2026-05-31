import psycopg2 as pg

def get_connection():
    conn = pg.connect("dbname=personal_finance user=postgres password=krish@psql")
    print("Database is connected")
    return conn