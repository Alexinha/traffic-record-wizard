##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################

''' This is the controller. It controls the user interation with the database.'''
import sqlite3
from model.traffic_record import TrafficRecord

RETRIEVE_LIMIT_RECORDS_SCRIPT = 'SELECT * FROM TrafficRecords LIMIT ?'
RETRIEVE_ALL_RECORDS_SCRIPT = 'SELECT * FROM TrafficRecords;'
INSERT_RECORD_SCRIPT = '''
INSERT INTO TrafficRecords (section_id, highway, section, section_length, section_description, date, description, "group", "type", county, ptrucks, adt, aadt, direction, pct85, priority_points)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
RETRIEVE_RECORD_BY_ID = 'SELECT * FROM TrafficRecords WHERE id = ?'
UPDATE_RECORD_SCRIPT = 'UPDATE TrafficRecords SET section_id = ?, highway = ?, section = ?, section_length = ?, section_description = ?, date = ?, "description" = ?, "group" = ?, "type" = ?, county = ?, ptrucks = ?, adt = ?, aadt = ?, direction = ?, pct85 = ?, priority_points = ? WHERE id = ?'

DELETE_RECORD_BY_ID = 'DELETE FROM TrafficRecords WHERE id = ?'

def display_limit_records_from_db(conn, limit):
    '''
    Display a limited number of records from the TrafficRecords table in the database.

    :param conn: sqlite3.Connection object, the database connection.
    :param limit: int, maximum number of records to display.
    '''
    with conn:
        cursor = conn.execute(RETRIEVE_LIMIT_RECORDS_SCRIPT, (limit,))
        rows = cursor.fetchall()
        for row in rows:
            record_id = row[0]
            record = TrafficRecord(*row[1:])
            print(f"id: {record_id}, {record}")

def display_all_records_from_db(conn):
    '''
    Display all records from the TrafficRecords table in the database.

    :param conn: sqlite3.Connection object, the database connection.
    '''
    with conn:
        cursor = conn.execute(RETRIEVE_ALL_RECORDS_SCRIPT)
        rows = cursor.fetchall()
        for row in rows:
            record_id = row[0]
            record = TrafficRecord(*row[1:])
            print(f"id: {record_id}, {record}")
    print(f"total records: {len(rows)}")

def insert_new_record(conn, record_str):
    '''
    Insert a new record into the TrafficRecords table.

    :param conn: sqlite3.Connection object, the database connection.
    :param record_str: str, comma-separated string of record fields.
    '''
    try:
        with conn:
            record = create_traffic_record_from_user_input(record_str)
            conn.execute(INSERT_RECORD_SCRIPT, (
                record.section_id,
                record.highway,
                record.section,
                record.section_length,
                record.section_description,
                record.date,
                record.description,
                record.group,
                record.type,
                record.county,
                record.ptrucks,
                record.adt,
                record.aadt,
                record.direction,
                record._85pct,
                record.priority_points
            ))
        print("New record inserted successfully.")
    except sqlite3.IntgrityError as e:
        print(f"Error inserting record: {e}")
    except Exception as e:
        print(f"Unexpected error happened: {e}")

def select_record_by_id(conn, record_id):
    '''
    Select and display a specific record from the database based on its ID.
    
    :param conn: sqlite3.Connection object, the database connection.
    :param record_id: int, ID of the record to select.
    :return: TrafficRecord object representing the selected record.
    '''
    with conn:
        cursor = conn.execute(RETRIEVE_RECORD_BY_ID, (record_id,))
        row = cursor.fetchone()
        if row:
            record = TrafficRecord(*row[1:])
            print(f"id: {row[0]}, {record}")
            return record
        else:
            print(f"No record found with ID: {record_id}")
            return None

def select_record_by_column_values(conn, table_name, criteria):
    '''
    Select records from the database based on given column-value 

    :param conn: sqlite3.Connection object, the database connection.
    :param table_name: str, the name of the table to search in. 
    :param search_criteria: list of SearchCriteria objects containing column names and values. 
    '''
    query = f'SELECT * FROM {table_name} WHERE '
    conditions = []
    values = []

    for c in criteria:
        conditions.append(f"{c.column_name} = ?")
        values.append(c.value)
    
    query += ' AND '.join(conditions)

    cursor = conn.execute(query, values)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            record_id = row[0]
            record = TrafficRecord(*row[1:])
            print(f"id: {record_id}, {record}")
    else:
        print("No records found matching the criteria.")

def edit_record_by_id(conn, record_id, record_str):
    '''
    Edit a specific record in the database based on its ID.
    
    :param conn: sqlite3.Connection object, the database connection.
    :param record_id: int, ID of the record to edit.
    :param record_str: str, comma-separated string of record fields.
    '''
    with conn:
        record = create_traffic_record_from_user_input(record_str)
        cursor = conn.execute(UPDATE_RECORD_SCRIPT, (
                record.section_id,
                record.highway,
                record.section,
                record.section_length,
                record.section_description,
                record.date,
                record.description,
                record.group,
                record.type,
                record.county,
                record.ptrucks,
                record.adt,
                record.aadt,
                record.direction,
                record._85pct,
                record.priority_points, 
                record_id))
        if cursor.rowcount > 0:
            print(f"Record with ID {record_id} updated successfully.")
        else:
            print(f"Failed to update record with ID: {record_id}. Record may not exist.")

def delete_record_by_id(conn, record_id):
    '''
    Delete a specific record from the database based on its ID.
    
    :param conn: sqlite3.Connection object, the database connection.
    :param record_id: int, ID of the record to delete.
    '''
    try:
        with conn:           
            cursor = conn.execute(DELETE_RECORD_BY_ID, (record_id,))
            if cursor.rowcount == 0:
                print(f"No record found with id {record_id}")
            else:
                print(f"Record with ID {record_id} deleted successfully.")         
    except sqlite3.Error as e:
        print(f"Error deleting record with id {record_id}: {e}")

def create_traffic_record_from_user_input(new_record_input):
    '''
    This is a helper function that converts a string from the user input into a TrafficRecord object.

    :param new_record_input: str, comma-separated string of record fields.
    :return: TrafficRecord object.
    '''
    fields = new_record_input.split(',')
    return TrafficRecord(*fields)