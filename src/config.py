# import dependencies
import csv as csv

# create class config
class Config:

    # Initialize Constructor
    def __init__(self, path):
        self.path = path

    # function to get csv location via file path and displays
    # the file path in a dictionary with 'path' as key
    def get_csv_system_location(self):

        csv_file_path = {}

        csv_file_path['path'] = self.path

        return csv_file_path

    # get csv data read it and organize each row of the data as
    # a 2d array for easy accessibility using indexes as keys
    def get_csv_data(self):
        data = []
        result = None

        csv_data = csv.reader(open(self.get_csv_system_location()['path']))
        for row in csv_data:
            data.append(row)

        return data;
