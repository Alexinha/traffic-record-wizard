##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part03       #
##################################

'''This is the test module for controller. It's designed to specifically test against database functionality.'''

import unittest
from controller.db_record_controller import delete_record_by_id, select_record_by_id
from workers.csv_handler import read_csv
from model.traffic_record import TrafficRecord
from workers.sqlite_func import db_connection

class TestDatabaseInteraction(unittest.TestCase):
    '''
    Unit test class for testing database interactions.
    '''

    def setUp(self):
        '''
        Set up an in-memory SQLite database and create the test table with test data.
        '''

        self.conn = db_connection(':memory:')
        self.create_test_table()
        self.insert_test_data()

    def tearDown(self):
        '''
        Close the database connection after each test.
        '''

        self.conn.close()
    
    def create_test_table(self):
        '''
        Create the TrafficRecords table in the in-memory database.
        '''

        create_table_script = '''
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
        self.conn.execute(create_table_script)
    
    def insert_test_data(self):
        '''
        Insert sample data into the TrafficRecords table.
        '''

        insert_script = '''
        INSERT INTO TrafficRecords (section_id, highway, section, section_length, section_description, date, description, "group", "type", county, ptrucks, adt, aadt, direction, pct85, priority_points)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        records = [
            ('1','395','30','11.71','STRATHLORNE-SCOTSVILLE RD (SCOTSVILLE) TO TK 19','05/15/2011','1.5 KM SOUTH OF TK 19','D','TC','INV','n/a','269','260','n/a','n/a', 'n/a'),
            ('2','395','31','11.72','STRATHLORNE-SCOTSVILLE RD (SCOTSVILLE) TO TK 19','05/16/2011','1.6 KM SOUTH OF TK 19','D','TC','INV','n/a','269','260','n/a','n/a', 'n/a'),
            ('3','395','32','11.73','STRATHLORNE-SCOTSVILLE RD (SCOTSVILLE) TO TK 19','05/17/2011','1.7 KM SOUTH OF TK 19','D','TC','INV','n/a','269','260','n/a','n/a', 'n/a'),
        ]
        for record in records:
            self.conn.execute(insert_script, record)
        self.conn.commit()
    
    def test_delete_record_by_id(self):
        '''
        Test the delete_record_by_id function to ensure it deletes a record correctly.
        '''

        #grab the id of the first record
        cursor = self.conn.execute('SELECT id FROM TrafficRecords LIMIT 1;')
        record_id_to_delete = cursor.fetchone()[0]
        delete_record_by_id(self.conn, record_id_to_delete)
        
        # Check if record with record_id_to_delete exists in the database
        deleted_record = select_record_by_id(self.conn, record_id_to_delete)
        self.assertIsNone(deleted_record, f"Record with ID {record_id_to_delete} still exists in the database.")
