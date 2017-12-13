'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''

# import dependencies
import os
import csv
import json
import time
import random
import requests
import pandas as pd
from termcolor import colored, cprint


class Sort:
    # Constructor
    def __init__(self, path):
        self.path = path
        self.start_time = time.time()
        self.data = self.csv_data_to_json()
        self.headers = self.get_csv_data()[0]
        self.start()

    def csv_data_to_json(self):
        f = open( self.path, 'r' )
        reader = csv.DictReader( f)
        result = json.dumps( [ row for row in reader ] )
        result = json.loads(result)
        self.data = result
        return result

    # search for any data by its key, and search value which can
    # be a string or integer
    # returns an array of all the data that matches the search field and
    # its relating row / information
    # used only afer the first time searching(!!important!!)
    def search(self, search_criteria, search_value):
        sorted_data = self.data
        self.print_execution('  ⌕ Searching For ' + str(search_value) +
                             ' in All `' + search_criteria + '` Field Of Csv Data...  ')
        result = []

        if(type(search_value).__name__ == 'list'):
            for i in range(len(sorted_data)):
                check = sorted_data[i][search_criteria]
                search_value[0] = self.set_data_type(check, search_value[0])
                search_value[1] = self.set_data_type(check, search_value[1])
                if check.isdigit() and check.find('.') != -1:
                    check = float(sorted_data[search_criteria][i])
                if(check > search_value[0] and check <= search_value[1]):
                    result.append(sorted_data[i])
                self.print_execution_completed('  ✓ Search Completed....  ')
                self.data = result
                return result
        else:
            for i in range(len(sorted_data)):
                check = sorted_data[i][search_criteria]
                search_value = self.set_data_type(check, search_value)
                if(check == search_value):
                    result.append(sorted_data[i])
            self.print_execution_completed('  ✓ Search Completed....  ')
            self.data = result
            return result

    def contains(self, search_criteria, search_value):
        sorted_data = self.data
        self.print_execution('  ⌕ Checking If ' + str(search_value) +
                             ' Is Contained In `' + search_criteria + '` Field Of Csv Data...  ')
        result = []
        for i in range(len(sorted_data)):
            check = sorted_data[i][search_criteria]
            search_value = self.set_data_type(check, search_value)
            if(check.lower().find(search_value.lower()) != -1):
                result.append(sorted_data[i])
        self.print_execution_completed('  ✓ Search Completed....  ')
        self.data = result
        return result

    # list of all search criterias that could be used
    def return_all_criterias(self):
        return self.headers

    # returns maximum number in a sorted csv data set
    # the search_field should always be an int (important!!)
    # parameter 2 is already soreted data (important!!)
    def get_maximum_value(self, search_field):
        sorted_data = self.data
        result = []
        if(sorted_data and len(sorted_data) > 0):
            maximum_num = 0
            value = sorted_data[0][search_field]
            if(value and value.isdigit and value.find('.') != -1):
                maximum_num = float(sorted_data[0][search_field])
            else:
                maximum_num = int(sorted_data[0][search_field])
            for i in range(len(sorted_data)):
                value = sorted_data[i][search_field]
                if(value and value.isdigit and value.find('.') != -1):
                    if(value == '.'):
                        value = 0.00
                    maximum_num = max(maximum_num, float(value))
                elif(value):
                    maximum_num = max(maximum_num, int(value))

            for i in range(len(sorted_data)):
                value = sorted_data[i][search_field]
                if(value and value.isdigit and value.find('.') != -1):
                    if(value == '.'):
                        value = 0.00
                    if(float(value) == maximum_num):
                        result.append(sorted_data[i])
                elif(int(value) == maximum_num):
                    result.append(sorted_data[i])
            self.data = result
            return result

    # returns minimum number in a sorted csv data set
    # the search_field should always be an int (important!!)
    # parameter 2 is already soreted data (important!!)
    def get_minimum_value(self, search_field):
        sorted_data = self.data
        result = []
        if(sorted_data and len(sorted_data) > 0):
            minimum_num = float(sorted_data[0][search_field])
            value = sorted_data[0][search_field]
            if(value and value.isdigit and value.find('.') != -1):
                minimum_num = float(sorted_data[0][search_field])
            else:
                minimum_num = int(sorted_data[0][search_field])
            for i in range(len(sorted_data)):
                value = sorted_data[i][search_field]
                if(value and value.isdigit and value.find('.') != -1):
                    if(value == '.'):
                        value = 0.00
                    minimum_num = min(minimum_num, float(value))
                elif(value):
                    minimum_num = min(minimum_num, int(value))

            for i in range(len(sorted_data)):
                value = sorted_data[i][search_field]
                if(value and value.isdigit and value.find('.') != -1):
                    if(value == '.'):
                        value = 0.00
                    if(float(value) == minimum_num):
                        result.append(sorted_data[i])
                elif(int(value) == minimum_num):
                    result.append(sorted_data[i])
            self.data = result
            return result

    # compares two data types and converts the data type of the
    # the first parameter as the data type of the second an returns it
    def set_data_type(self, check, search_value):
        result = None
        if(type(check).__name__ == 'str'):
            result = str(search_value)
            if(check.isdigit() and check.find('.') != -1):
                result = float(search_value)
        else:
            result = int(search_value)
        return result

    # display data in a table like in excel
    def display_data_as_table(self):
        return pd.DataFrame(self.data)

    # get number of colums
    def get_col_number(self):
        return len(self.headers)

    # get number of rows
    def get_row_number(self):
        return len(self.data)

    # print formated json data of csv infomation to a given (filename).json
    def print_filtered_json_tofile(self, name_of_file):
        data = self.data
        self.print_execution(
            '  🖨  Printing Sorted Data To File (' + str(name_of_file) + '.json)...  ')
        directory = './filtered_data/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + name_of_file + '.json', 'w') as outfile:
            json.dump(data, outfile)

    # Delete Json file
    def delete_json_file(self, filepath):
        self.print_execution(
            '  🔪  Deleting File (' + filepath + '.json)...  ')
        os.remove('./filtered_data/' + filepath + '.json')

    # Delete Csv File
    def delete_csv_file(self, filepath):
        self.print_execution(
            '  🔪  Deleting File (' + filepath + ')...')
        if '.csv' in filepath:
            os.remove('../resources/' + filepath)
        else:
            os.remove('../resources/' + filepath + '.csv')

    # print list with bullet points / arrows
    def print_all_search_fields(self, message, all_search_fields):
        sorted_data = self.data
        key = None
        print(colored(message, 'grey', 'on_white', attrs=['bold']))
        print('----------------------------------------')
        length_of_field = len(sorted_data)
        pick_random_field = random.randint(0, length_of_field)
        for i in range(len(all_search_fields)):
            arrows = colored('⎸►| ', 'magenta')
            key = all_search_fields[i]
            print(
                arrows + colored(all_search_fields[i] + ' ➾ ' + sorted_data[pick_random_field][all_search_fields[i]], 'cyan', attrs=['bold']))
        print('----------------------------------------')
        data_len = str(len(sorted_data))
        cprint('         Length Of Csv Data is ' +
               data_len + '     ', 'white', 'on_magenta')

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
        csv_data = csv.reader(open(self.get_csv_system_location()['path']))
        for row in csv_data:
            data.append(row)
        return data

    # print colored paramter / arguement passed in
    # intended for execution messages while program is running
    def print_execution(self, message):
        cprint(message, 'grey', attrs=['bold'])

    # print colored paramter / arguement passed in
    # intended for end execution of proccess
    def print_execution_completed(self, message):
        cprint(message, 'magenta', attrs=['bold'])

    # Print headers
    def start(self):
        print('\n')
        print('----------------------------------------')
        cprint('        ⛹  Data Playground ⛹            ', 'white', 'on_magenta')
        print('----------------------------------------')
        self.print_execution('  📚  Sorting Data...  ')
        self.print_execution_completed('  ✓ Csv File Imported Successfully  ')
        # prints out all search fields / criterias that
        # can be used to filter the csv data imported
        message = '    Snippet Of The Data Csv Imported    '
        self.print_all_search_fields(message, self.headers)
        print('----------------------------------------')

    def send_data_as_post(self, url):
        data = self.data
        if(len(data) > 0):
            self.print_execution(
                '  📩  Sending Data To The Web For Vizualization  ')
            headers = {'X-Requested-With': 'XMLHttpRequest'}
            post_data = {'mapData': json.dumps(data)}
            post = requests.post(url=url, headers=headers, data=post_data)
            self.print_execution_completed(
                '  📬  Data Sent Successfully ')
            return post

    # pretty print end of excecution time
    def end(self):
        end = time.time()
        total_time = str(round(end - self.start_time, 3))
        print('----------------------------------------')
        self.print_execution('            ⏳ Execution Time           ')
        cprint('             ' + total_time +
               ' second(s)             ', 'white', 'on_magenta')
        print('----------------------------------------')

    def convert_json_to_array(self):
        headers = self.headers
        data = self.data
        result = []
        for i in range(len(self.headers)):
            current_header = []
            for j in range(len(self.data)):
                header_at_index = self.data[j][self.headers[i]]
                current_header.append(header_at_index)
            result.append(current_header)
        return result
