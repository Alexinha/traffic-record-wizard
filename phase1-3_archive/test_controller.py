##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part02       #
##################################

'''This is the test module for controller'''

import os
import unittest
from controller.record_controller import delete_record, write_records_to_disk
from workers.csv_handler import read_csv
from model.traffic_record import TrafficRecord

class TestRecordController(unittest.TestCase):
    def setUp(self):
        '''
        This function sets up initial conditions for the tests.
        It creates a list of TrafficRecord objects to be used in the tests and stores them in a local file.
        '''
        self.records = [
            TrafficRecord('1','395','30','11.71','STRATHLORNE-SCOTSVILLE RD (SCOTSVILLE) TO TK 19','05/15/2011','1.5 KM SOUTH OF TK 19','D','TC','INV','n/a','269','260','n/a','n/a', 'n/a'),
            TrafficRecord('2','395','31','11.72','STRATHLORNE-SCOTSVILLE RD (SCOTSVILLE) TO TK 19','05/16/2011','1.6 KM SOUTH OF TK 19','D','TC','INV','n/a','269','260','n/a','n/a', 'n/a'),
            TrafficRecord('3','395','32','11.73','STRATHLORNE-SCOTSVILLE RD (SCOTSVILLE) TO TK 19','05/17/2011','1.7 KM SOUTH OF TK 19','D','TC','INV','n/a','269','260','n/a','n/a', 'n/a'),
        ]

        self.test_file = 'test_records.csv'
        write_records_to_disk(self.test_file, self.records)

    def tearDown(self):
        '''
        This function cleans up the testing files written to local after the test
        '''
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_delete_record(self):
        '''
        This is a test case for removing a record with a given index from the memory and any provided user-saved files
        '''
        records_length = len(self.records)

        # Delete the first record
        delete_record(1, self.records, self.test_file)

        # check if the length has changed by one
        self.assertEqual(len(self.records), records_length - 1)

        # check that the removed record is no longer in the local file 
        removed_section_id = '1'
        updated_records_in_file = read_csv(self.test_file, 3)
        for record in updated_records_in_file: 
            self.assertNotEqual(record.section_id, removed_section_id)
