##################################
# Name: Jingxuan Chang           #
# Number: 041058102              #
# Course: CST8333                #
# Practical Project Part04       #
##################################

'''This is the Model, it represents a traffic record object.'''

class TrafficRecord:
    
    def __init__(self, section_id, highway, section, section_length, section_description, date, description, group, type, county, ptrucks, adt, aadt, direction, _85pct, priority_points):
        '''
        This is the constructor to initialize the TrafficRecord objectwith provided attributes.
        '''
        self.section_id = section_id
        self.highway = highway
        self.section = section
        self.section_length = section_length
        self.section_description = section_description
        self.date = date
        self.description = description if description else 'n/a'
        self.group = group if group else 'n/a'
        self.type = type if type else 'n/a'
        self.county = county if county else 'n/a'
        self.ptrucks = ptrucks if ptrucks else 'n/a'
        self.adt = adt if adt else 'n/a'
        self.aadt = aadt if aadt else 'n/a'
        self.direction = direction if direction else 'n/a'
        self._85pct = _85pct if _85pct else 'n/a'
        self.priority_points = priority_points if priority_points else 'n/a'

    def __str__(self):
        '''
        This is the string representation of the TrafficRecord object
        '''
        return f"Section ID: {self.section_id}, Highway: {self.highway}, Section: {self.section}, Section Length: {self.section_length}, Section Description: {self.section_description}, Date: {self.date}, Description: {self.description}, Group: {self.group}, Type: {self.type}, County: {self.county}, PTrucks: {self.ptrucks}, ADT: {self.adt}, AADT: {self.aadt}, Direction: {self.direction}, 85PCT: {self._85pct}, Priority Points: {self.priority_points}"