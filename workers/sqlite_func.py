##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################

''' This module handles initialization works for database connection. It includes database connection, table creation, and populating data into the table(s). '''
import sqlite3
from workers.csv_handler import read_csv
from model.traffic_record import TrafficRecord

CREATE_TABLE_SCRIPT = '''
CREATE TABLE IF NOT EXISTS TrafficRecords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_id TEXT, 
    highway TEXT, 
    section TEXT, 
    section_length TEXT, 
    section_description TEXT, 
    date TEXT, 
    "description" TEXT, 
    "group" TEXT, 
    "type" TEXT, 
    county TEXT, 
    ptrucks TEXT, 
    adt TEXT, 
    aadt TEXT, 
    direction TEXT, 
    pct85 TEXT, 
    priority_points TEXT
)'''

INSERT_RECORD_SCRIPT = '''
INSERT INTO TrafficRecords (section_id, highway, section, section_length, section_description, date, description, "group", "type", county, ptrucks, adt, aadt, direction, pct85, priority_points)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

DELETE_ALL_SCRIPT = 'DELETE FROM TrafficRecords;'

# create or connect to traffic.db
def db_connection(db = 'traffic.db'):
    '''
    Establishes a connection to the SQLite database.

    :param db: str, filename of the SQLite database.
    :return: sqlite3.Connection object, the database connection.
    '''
    return sqlite3.connect(db)

# create a traffic record table
def create_table(conn):
    '''
    Creates the TrafficRecords table in the database if it doesn't exist.

    :param conn: sqlite3.Connection object, the database connection.
    '''
    with conn:
        #conn.execute('DROP TABLE IF EXISTS TrafficRecords;')
        conn.execute(CREATE_TABLE_SCRIPT)

# function to insert one record
def insert_record(conn, record):
    '''
    Inserts a single TrafficRecord object into the TrafficRecords table.

    :param conn: sqlite3.Connection object, the database connection.
    :param record: TrafficRecord object, the record to insert.
    '''
    with conn:
        conn.execute(INSERT_RECORD_SCRIPT, (
            record.section_id, record.highway, record.section, record.section_length, record.section_description, record.date, record.description, record.group, record.type, record.county, record.ptrucks, record.adt, record.aadt, record.direction, record._85pct, record.priority_points
            ))

# function to populate or reload database from csv file
def reload_db_from_csv(filename, conn, max_records=None):
    '''
    Deletes all existing records in the database and reloads it with data from a CSV file.

    :param filename: str, filename of the CSV file containing data.
    :param conn: sqlite3.Connection object, the database connection.
    :param max_records: int, optional, maximum number of records to load from the CSV.
    '''
    delete_all_records(conn)
    print('loading ... ... \n')
    records = read_csv(filename, max_records)
    for record in records:
        insert_record(conn, record)
    print('\ndata from csv populated into database\n')

# function to clean up all data in the db 
def delete_all_records(conn):
    '''
    Deletes all records from the TrafficRecords table in the database.

    :param conn: sqlite3.Connection object, the database connection.
    '''
    try:
        conn.execute(DELETE_ALL_SCRIPT)
        print('\ndata in db cleaned up\n')
    except sqlite3.Error as e:
        print(e)

