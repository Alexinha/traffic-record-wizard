##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################

'''Module for handling CS files and traffic records by reading and printing.'''
import csv
from model.traffic_record import TrafficRecord

def read_csv(filename, max_records=None):
    '''
    This function reads traffic records from a CSV file and returns a list of TrafficRecord objects.
    
    :param filename str: The name of the CSV file to read.
    :return: a list of TrafficRecord objects.
    '''
    records = [];
    try: 
        # open the csv file that is in the same directory as this py file in read mode
        with open(filename, 'r') as csv_file: 
            # create a csv reader object 
            # by using DictReader, data in csv file is tightly associated to its column name
            csv_reader = csv.DictReader(csv_file)
            for index, line in enumerate(csv_reader):
                if max_records is not None and index >= max_records:
                    break;
                # create a TrafficRecord object for each line and append it to the records list
                record = TrafficRecord(
                    section_id=line['SECTION ID'],
                    highway=line['HIGHWAY'],
                    section=line['SECTION'],
                    section_length=line['SECTION LENGTH'],
                    section_description=line['SECTION DESCRIPTION'],
                    date=line['Date'],
                    description=line['DESCRIPTION'],
                    group=line['GROUP'],
                    type=line['TYPE'],
                    county=line['COUNTY'],
                    ptrucks=line['PTRUCKS'],
                    adt=line['ADT'],
                    aadt=line['AADT'],
                    direction=line['DIRECTION'],
                    _85pct=line['85PCT'],
                    priority_points=line['PRIORITY_POINTS']
                )
                records.append(record)
    except FileNotFoundError:
        # handle FileNotFoundError
        print("Error: File is not found.")
    # return the list of records after going through all the lines 
    return records