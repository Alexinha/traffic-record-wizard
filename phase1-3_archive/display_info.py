##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part02       #
##################################

'''This is the view, which handles the application presentation and interaction with user.'''

from controller.record_controller import create_traffic_record_from_user_input, get_traffic_records, print_records, reload_traffic_records, write_new_record_to_file, write_records_to_disk, display_specific_record, display_multiple_records, edit_record, delete_record
from model.traffic_record import TrafficRecord

def display_traffic_records(records):
    '''
    This function calls displays records in the console.
    
    :param records: list, list of TrafficRecord objects to be displayed.
    '''
    print('\nPrinting traffic records ... \n')
    print_records(records)

def display_menu(filename, max_records, records):
    '''
    This function displays the menu for interacting with traffic records.
    It provides options to reload data, create a file, add a new record, display specific records, edit or delete records, and more.

    :param filename: str, the name of the CSV file to read from or write to.
    :param max_records: int, the maximum number of records to handle.
    :param records: list, list of TrafficRecord objects.
    '''
    print('\nPlease select an option number. Enter anything else to exit the program.\n')
    while True: 
        print('\n*************************\n')
        print('1. Reload the data.\n')
        print('2. Create a file and store the first 100 records into it.\n')
        print('3. Add a new record.\n')
        print('4. Display one selected record.\n')
        print('5. Display selected records in a given index range.\n')
        print('6. Select one record and edit.\n')
        print('7. Select one record and delete.\n')
        print('\n*************************\n')
        option = input('option: ')
        if option == '1': 
            records = reload_traffic_records(filename, max_records)
            print_records(records)
        elif option == '2':
            print('create a file name here, or overwite an existing one.\n')
            new_file_name = input('new file name: ')
            write_records_to_disk(new_file_name, records)
        elif option == '3':
            print('create a file name here, or add record to an existing one.\n')
            file_name = input('file name: ')
            print('Enter the new record you would like to add, using comma to separate each field.\n')
            new_record_input = input('new record: ')
            new_record = create_traffic_record_from_user_input(new_record_input)
            write_new_record_to_file(file_name, new_record, records)
        elif option == '4':
            index = int(input('Enter the index of the record: '))
            display_specific_record(index, records)
        elif option == '5':
            indexStart = int(input('Index start from: '))
            indexEnd = int(input('Index ends at: '))
            display_multiple_records(indexStart, indexEnd, records)
        elif option == '6':
            index = int(input('Enter the index of the record: '))
            edit_record(index, records)
            save_option = input('Would you like to save it to disk? Press Y to save, others to exit: ').lower()
            if save_option == 'y':
                filename = input('type the file name again: ')
                write_records_to_disk(filename, records)
        elif option == '7':
            index = int(input('Enter the index of the record: '))
            filename = input('\nProvide the filename you would like to delete the record from: ')
            delete_record(index, records, filename)
        else:
            break

