import sqlite3
from sqlite3 import Error


def init_database(db_file):
    conn, cursor = get_cursor(db_file)
    sql_create_order_table = """ CREATE TABLE IF NOT EXISTS flights (
                                                    flight_id integer PRIMARY KEY AUTOINCREMENT,
                                                    from_city text NOT NULL,
                                                    to_city text NOT NULL,
                                                    price text,
                                                    available_seats integer,
                                                    date text
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
            ('NRT', 'EDI', '3190', '9', '2024-03-27'),
            ('EDI', 'NRT', '3180', '5','2024-03-27'),
            ('OXF', 'EDI', '190','6','2024-03-28'),
            ('EDI', 'BMX', '110','10','2024-03-28'),
            ('LHR', 'EDI', '140', '30','2024-03-27'),
            ('EDI', 'OXF', '120', '0','2024-03-27'),
            ('NRT', 'EDI', '3190', '9', '2024-03-27'),
            ('EDI', 'NRT', '3180', '5', '2024-03-27'),
            ('OXF', 'EDI', '190', '6', '2024-03-27'),
            ('EDI', 'BMX', '110', '10', '2024-03-27'),
            ('LHR', 'EDI', '140', '30', '2024-03-27'),
            ('EDI', 'OXF', '120', '0', '2024-03-27'),
            ('NRT', 'EDI', '3190', '19', '2024-03-27'),
            ('EDI', 'NRT', '3180', '15','2024-03-27'),
            ('OXF', 'EDI', '190','16','2024-03-28'),
            ('EDI', 'BMX', '110','20','2024-03-28'),
            ('LHR', 'EDI', '140', '33','2024-03-28'),
            ('EDI', 'OXF', '120', '2','2024-03-28'),
            ('NRT', 'EDI', '3190', '19', '2024-03-30'),
            ('EDI', 'NRT', '3180', '51', '2024-03-30'),
            ('OXF', 'EDI', '190', '61', '2024-03-30'),
            ('EDI', 'BMX', '110', '11', '2024-03-30'),
            ('LHR', 'EDI', '140', '0', '2024-04-1'),
            ('EDI', 'OXF', '120', '1', '2024-04-2')
        ]

        # Loop through the list and execute the INSERT statement for each tuple
        for flight_data in flights_data:
            cursor.execute(
                'INSERT INTO flights (from_city, to_city, price, available_seats,date) VALUES (?, ?, ?, ?, ?)', flight_data)

        # Commit the transaction after all inserts
        conn.commit()
    except Error as e:
        print(e)


def get_flights(db_file, from_city, to_city, from_date):
    print("test")
    print("in DB", from_city, to_city, from_date)
    list_sql = "SELECT * FROM flights WHERE from_city = ? AND to_city = ? AND date = ?"
    conn, cursor = get_cursor(db_file)

    try:
        cursor.execute(list_sql, (from_city, to_city,from_date))
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        cursor.close()
        return records

    except Error as e:
        print(e)
