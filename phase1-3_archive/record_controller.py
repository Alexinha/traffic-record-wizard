##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part02       #
##################################

'''This is the Controller, which handles activities to do with traffic volumes records.'''

import csv
import os
from workers.csv_handler import read_csv
from model.traffic_record import TrafficRecord

# this is the global variable that holds the records 
records = []

def get_traffic_records(filename, max_records):
    '''
    This function calls CSV handler to read in a given amount of records.
    :param filename: str, the name of the CSV file to read.
    :param max_records: int, the maximum number of records to read.
    :return: list of TrafficRecord objects.
    '''
    records = read_csv(filename, max_records)
    return records

def print_records(records):
    '''
    This function iterates over each record in a records list and prints them.
    
    :param records: list, a list of TrafficRecord objects
    '''
    for record in records:
        print(record)
    print("total records: " + str(len(records)))

def reload_traffic_records(filename, max_records):
    '''
    This function re-read the records from the csv file and re-populate the records list with the original data.
    :param filename: str, the name of the CSV file to read.
    :param max_records: int, the maximum number of records to read.
    :return: list of reloaded TrafficRecord objects.
    '''
    records = []
    print('records cleared')
    records = read_csv(filename, max_records)
    print('records reloaded')
    return records

# when user choose to do create a file to store the record displayed
def write_records_to_disk(filename, records):
    '''
    This function saves the records displayed to a local file with the filename user gives.
    
    :param filename: str, the name of the file to save the records to.
    :param records: list, list of TrafficRecord objects to save.
    '''
    try:
        with open(filename, 'w', newline='') as csvfile:
            recordwriter = csv.writer(csvfile)
            # write the titles first 
            recordwriter.writerow(['SECTION ID', 'HIGHWAY', 'SECTION', 'SECTION LENGTH', 'SECTION DESCRIPTION', 'Date', 
                'DESCRIPTION', 'GROUP', 'TYPE', 'COUNTY', 'PTRUCKS', 'ADT', 'AADT', 'DIRECTION', 
                '85PCT', 'PRIORITY_POINTS'])
            # write the records --- does it work with only one record?
            for record in records:
                recordwriter.writerow([record.section_id, record.highway, record.section, record.section_length,
                    record.section_description, record.date, record.description, record.group,
                    record.type, record.county, record.ptrucks, record.adt, record.aadt,
                    record.direction, record._85pct, record.priority_points])     
            print('Data written to ' + filename + '\n')    
    except FileNotFoundError:
        print('Error: File is not found.')

# when user choose to append a new record to the file they create 
def write_new_record_to_file(filename, record, records):
    '''
    This function adds a new record to a given file or creates a new file with the added record if it doesn't exist.

    :param filename: str, the name of the file to append the record to.
    :param record: TrafficRecord, TrafficRecord object to append.
    :param records: list, list of TrafficRecord objects to update in memory.
    :return: updated list of TrafficRecord objects.
    '''
    try: 
        # check if the record passed in is a record object 
        if not isinstance(record, TrafficRecord):
            print('Error: the record you typed in is not valid')
            return
        # if it is valid 
        # is there already a file? append 
        has_file = os.path.isfile(filename)
        if has_file: 
            # append to the file 
            with open(filename, 'a', newline='') as csvfile:
                recordwriter = csv.writer(csvfile)
                # append a row
                recordwriter.writerow([record.section_id, record.highway, record.section, record.section_length,
                    record.section_description, record.date, record.description, record.group,
                    record.type, record.county, record.ptrucks, record.adt, record.aadt,
                    record.direction, record._85pct, record.priority_points])
            print('append new record to ' + filename + ' successfully')
        else: 
            # create new file and add titles 
            with open(filename, 'w', newline='') as csvfile:
                recordwriter = csv.writer(csvfile)
                # write the titles first 
                recordwriter.writerow(['SECTION ID', 'HIGHWAY', 'SECTION', 'SECTION LENGTH', 'SECTION DESCRIPTION', 'Date', 
                    'DESCRIPTION', 'GROUP', 'TYPE', 'COUNTY', 'PTRUCKS', 'ADT', 'AADT', 'DIRECTION', 
                    '85PCT', 'PRIORITY_POINTS'])
                # write the record
                recordwriter.writerow([record.section_id, record.highway, record.section, record.section_length,
                    record.section_description, record.date, record.description, record.group,
                    record.type, record.county, record.ptrucks, record.adt, record.aadt,
                    record.direction, record._85pct, record.priority_points])
            print(filename + ' has been created with new record added')
        records.append(record)
    except FileNotFoundError:
        print('Error: File is not found.')
    return records

def display_specific_record(index, records):
    '''
    This function displays a specific record from the list based on the given index.

    :param index: int, the index of the record to display (1-based).
    :param records: list, list of TrafficRecord objects.
    '''
    try:
        record = records[index - 1]
        print(record)
    except IndexError:
        print('Error: record with the given index does not exist.')

def display_multiple_records(range_start_index, range_end_index, records):
    '''
    This function displays multiple records from the list within the given index range.

    :param range_start_index: int, the starting index of the range given by user (starting from 1).
    :param range_end_index: int, the ending index of the range given by user (starting from 1).
    :param records: list, list of TrafficRecord objects.
    '''
    try:
        if range_end_index > len(records) or range_start_index < 1:
            print('range out of limit.\n')
            return
        for i in range(range_start_index - 1, range_end_index):
            print(records[i])
    except IndexError:
        print('Error: index range incorrect.')

# select and edit specific record
def edit_record(index, records):
    '''
    This function edits a specific record in the list based on the given index (starting from 1), and saves the result to disk.

    :param index: int, the index of the record to edit.
    :param records: list, list of TrafficRecord objects.
    '''
    try:
        record = records[index - 1]
        print('This is the record you would like to edit:\n')
        print(record)
        new_record_input = input('\nenter your edition, separate fields with comma: ')
        new_record = create_traffic_record_from_user_input(new_record_input)
        records[index - 1] = new_record
        print('\nRecord edited.\n')
    except IndexError:
        print('Error: record with the given index does not exist.')

def delete_record(index, records, filename):
    '''
    This function removes a specific record in the list based on the given index (starting from 1), and saves the result to disk.

    :param index: int, the index of the record to delete.
    :param records: list, list of TrafficRecord objects.
    '''
    try: 
        records.pop(index - 1)
        write_records_to_disk(filename, records)
        print('record deleted\n')
    except IndexError:
        print('Error: record with the given index does not exist.')

def create_traffic_record_from_user_input(new_record_input):
    '''
    This is a helper function that convers a string from the user input into a TrafficRecord object.

    :param new_record_input: str, comma-separated string of record fields.
    :return: TrafficRecord object.
    '''
    fields = new_record_input.split(',')
    return TrafficRecord(*fields)