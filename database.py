import sqlite3
from sqlite3 import Error


def init_database(db_file):
    conn, cursor = get_cursor(db_file)
    sql_create_order_table = """ CREATE TABLE IF NOT EXISTS flights (
                                                    flight_id integer PRIMARY KEY AUTOINCREMENT,
                                                    from_city text NOT NULL,
                                                    to_city text NOT NULL,
                                                    price text
                                                ); """

    try:
        cursor.execute(sql_create_order_table)
    except Error as e:
        print(e)
    insert_order(db_file)


def get_cursor(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor


def insert_order(db_file):
    conn, cursor = get_cursor(db_file)
    try:
        # List of tuples containing values to insert
        flights_data = [
            ('NRT', 'LHR', '20'),
            ('ABC', 'XYZ', '30'),
            ('DEF', 'GHI', '40')
            # Add more tuples as needed
        ]

        # Loop through the list and execute the INSERT statement for each tuple
        for flight_data in flights_data:
            cursor.execute("INSERT INTO flights (from_city, to_city, price) VALUES (?, ?, ?)", flight_data)

        # Commit the transaction after all inserts
        conn.commit()
    except Error as e:
        print(e)


def get_flights(db_file, flight):
    list_sql = "SELECT * FROM flights WHERE from_city = 'NRT'"
    conn, cursor = get_cursor(db_file)

    try:
        cursor.execute(list_sql)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        cursor.close()
        return records

    except Error as e:
        print(e)
