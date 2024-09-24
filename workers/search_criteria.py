##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################

class SearchCriteria:
    '''
    Represents a search critera object for querying the database.

    Attributes:
        column_name: str, the name of the column to search in.
        value: str, the value to search for in the column. 
    '''
    def __init__(self, column_name, value):
        '''
        Initializes a new SearchCriteria object with the specified column name and value. 

        :param column_name: str, the name of the column to search in.
        :param value: str, the value to search for in the column. 
        '''
        self.column_name = column_name
        self.value = value
    def __str__(self):
        '''
        Returns a string representation of the SearchCriteria object.

        :return: str, a formatted string showing the column name and value.
        '''
        return f"{self.column_name}: {self.value}"