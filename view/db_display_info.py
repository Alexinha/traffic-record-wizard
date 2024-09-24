##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################

'''This is the view, which handles the application presentation and interaction with user.'''

from controller.db_record_controller import create_traffic_record_from_user_input, delete_record_by_id, display_all_records_from_db, edit_record_by_id, insert_new_record, select_record_by_column_values, select_record_by_id
from model.traffic_record import TrafficRecord
from workers.search_criteria import SearchCriteria
from workers.sqlite_func import reload_db_from_csv

def display_menu(filename, conn):
    '''
    Display a menu to allow users to interact with the database.

    :param filename: str, filename of the CSV file to reload data from.
    :param conn: sqlite3.Connection object, the database connection.
    '''
    print('\nPlease select an option number. Enter anything else to exit the program.\n')
    
    while True: 
        print('\n*************************\n')
        print('1. Reload the database.\n')
        print('2. Display all the records in the database.\n')
        print('3. Add a new record.\n')
        print('4. Display one record by id.\n')
        print('5. Update one record by id.\n')
        print('6. Delete one record by id.\n')
        print('7. Select records by column values.\n')
        print('\n*************************\n')
        option = input('option: ')
        if option == '1': 
            reload_db_from_csv(filename, conn, None)

        elif option == '2':
            display_all_records_from_db(conn)

        elif option == '3':
            print('Enter the new record you would like to add, using comma to separate each field.\n')
            new_record_input = input('new record: ')
            insert_new_record(conn, new_record_input)
            
        elif option == '4':
            record_id = input('Enter the id of the record: ')
            select_record_by_id(conn, record_id)
            
        elif option == '5':
            record_id = input('Enter the id of the record you would like to update: ')
            print('Enter the updated record, using comma to separate each field.\n')
            updated_record = input('updated record: ')
            edit_record_by_id(conn, record_id, updated_record)

        elif option == '6':
            record_id = input('Enter the id of the record you would like to delete: ')
            delete_record_by_id(conn, record_id)

        elif option == '7':
            search_criteria = []   
            # asking the user for column - value until user explicitly break out the loop       
            while True:     
                column_name = input('enter column name: ').strip()
                column_value = input("enter value for column: ").strip()
                continue_flag = input("Enter one more column search criteria? Y/N: ")
                # append each SearchCriteria object to the array
                search_criteria.append(SearchCriteria(column_name, column_value))
                # only break the loop when the appending is done!!
                if continue_flag.lower() != 'y':
                    break

            select_record_by_column_values(conn, 'TrafficRecords', search_criteria)
            # for c in search_criteria:
            #     print(c)
            
        else:
            break

