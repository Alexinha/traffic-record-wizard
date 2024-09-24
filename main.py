##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################
'''
Main module for reading and printing traffic records from CSV file.
'''
from controller.db_record_controller import delete_record_by_id, display_all_records_from_db, display_limit_records_from_db, edit_record_by_id, insert_new_record, select_record_by_id
from workers.sqlite_func import create_table, db_connection, delete_all_records, reload_db_from_csv
from view.db_display_info import display_menu

def main():
    '''
    This is the main function to read and print traffic records.
    '''
    credential = f"\nAuthor:\nJingxuan Chang\n041058102\nCST8333"
    # print student/course information 
    print('This is practical practice 04')
    print(credential)
    # set the csv file path that we read in 
    SOURCE_FILE = 'Traffic_Volumes_Provincial_Highway_System.csv'

    #NEW_RECORD='8888,1,47,4.5,PATTON RD (SACKVILLE) TO MOUNT UNIACKE CONN,07/13/2023,0.5 KM EAST OF BRUSHY HILL RD,A,TC,HFX,,3039,2650,,,'

    #UPDATE_RECORD='1000,1,47,4.5,PATTON RD (SACKVILLE) TO MOUNT UNIACKE CONN,07/13/2023,0.5 KM EAST OF BRUSHY HILL RD,A,TC,HFX,,3039,2650,,,'

    conn = db_connection()
    
    create_table(conn)
    
    #populate the database, initialize data, run once and for all unless reload is needed
    #reload_db_from_csv(SOURCE_FILE, conn, None)

    # display the menu in the end 
    display_menu(SOURCE_FILE, conn)

    conn.commit()
    conn.close()
    print('database closed')


# only call the main function when the script is executed directly
if __name__ == '__main__':
    main()