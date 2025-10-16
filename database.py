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
                                                    date text,
                                                    time text
                                                ); """

    try:
        cursor.execute(sql_create_order_table)
    except Error as e:
        print(e)
    insert_order(db_file)
    sql_create_order_table = """ CREATE TABLE IF NOT EXISTS customers (
                                                        id integer PRIMARY KEY AUTOINCREMENT,
                                                        first_name text NOT NULL,
                                                        second_name text NOT NULL,
                                                        last_name text NOT NULL,
                                                        phone_number text NOT NULL,
                                                        email_address text NOT NULL,
                                                        address text NOT NULL
                                                    ); """
    try:
        cursor.execute(sql_create_order_table)
    except Error as e:
        print(e)


def get_cursor(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor


def insert_order(db_file):
    conn, cursor = get_cursor(db_file)
    try:
        # List of tuples containing values to insert
        flights_data = [
            ('NRT', 'EDI', '3190', '9', '2026-04-27', '10:00'),
            ('EDI', 'NRT', '3180', '5', '2026-04-27', '20:00'),
            ('OXF', 'EDI', '190', '6', '2026-04-28', '3:00'),
            ('OXF', 'EDI', '190', '6', '2026-04-30', '3:00'),
            ('EDI', 'BMX', '110', '10', '2026-04-28', '11:00'),
            ('LHR', 'EDI', '140', '30', '2026-04-27', '12:00'),
            ('EDI', 'OXF', '120', '0', '2026-04-27', '13:00'),
            ('NRT', 'EDI', '3190', '9', '2026-04-27', '19:00'),
            ('EDI', 'NRT', '3180', '5', '2026-04-28', '13:00'),
            ('OXF', 'EDI', '190', '6', '2026-04-27', '21:00'),
            ('EDI', 'BMX', '110', '10', '2026-04-27', '06:00'),
            ('LHR', 'EDI', '140', '30', '2026-04-27', '10:00'),
            ('EDI', 'OXF', '120', '0', '2026-04-27', '15:00'),
            ('NRT', 'EDI', '3190', '19', '2026-04-27', '18:00'),
            ('EDI', 'NRT', '3180', '15', '2026-04-27', '19:00'),
            ('BMX', 'EDI', '190', '16', '2026-04-28', '14:00'),
            ('EDI', 'BMX', '110', '20', '2026-04-28', '11:00'),
            ('LHR', 'EDI', '140', '33', '2026-04-28', '10:00'),
            ('LHR', 'BRS', '140', '33', '2026-04-27', '10:00'),
            ('EDI', 'OXF', '120', '2', '2026-04-28', '10:00'),
            ('NRT', 'EDI', '3190', '19', '2026-04-30', '12:00'),
            ('EDI', 'NRT', '3180', '51', '2026-04-30', '18:00'),
            ('OXF', 'EDI', '190', '61', '2026-04-30', '10:30'),
            ('EDI', 'BMX', '110', '11', '2026-04-30', '16:00'),
            ('LHR', 'EDI', '140', '0', '2026-05-1', '22:00'),
            ('EDI', 'OXF', '120', '1', '2026-05-2', '23:00'),
            ('BRS', 'LHR', '100', '3', '2026-04-28', '10:00')
        ]

        # Loop through the list and execute the INSERT statement for each tuple
        for flight_data in flights_data:
            cursor.execute(
                'INSERT INTO flights (from_city, to_city, price, available_seats,date,time) VALUES (?, ?, ?, ?, ?,?)',
                flight_data)

        # Commit the transaction after all inserts
        conn.commit()
    except Error as e:
        print(e)


def get_booked_flight(db_file, flight_id):
    list_sql = "SELECT * FROM flights WHERE flight_id= ?"
    conn, cursor = get_cursor(db_file)

    try:
        cursor.execute(list_sql, (flight_id,))
        records = cursor.fetchall()
        cursor.close()
        return records

    except Error as e:
        print(e)


def get_flights(db_file, from_city, to_city, from_date):
    list_sql = "SELECT * FROM flights WHERE from_city = ? AND to_city = ? AND date = ?"
    conn, cursor = get_cursor(db_file)
    print(from_city, to_city, from_date)
    try:
        cursor.execute(list_sql, (from_city, to_city, from_date))
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        cursor.close()
        return records

    except Error as e:
        print(e)


def add_pasenger(db_file, first_name, second_name, last_name, phone_number, email_address, address):
    conn, cursor = get_cursor(db_file)

    cursor.execute(
        'INSERT INTO customers (first_name, second_name, last_name, phone_number,email_address,address) VALUES (?, ?, ?, ?, ?,?)',
        [first_name, second_name, last_name, phone_number, email_address, address])

    # Commit the transaction after all inserts
    conn.commit()


def get_passenger(db_file):
    print("test customer")

    list_sql = "SELECT * FROM customers ORDER BY ID DESC LIMIT 1"
    conn, cursor = get_cursor(db_file)

    try:
        cursor.execute(list_sql)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        cursor.close()
        return records

    except Error as e:
        print(e)
