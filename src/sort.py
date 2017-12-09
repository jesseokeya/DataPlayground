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
        self.data = self.get_csv_data()
        self.headers = self.data[0]
        self.start()

    def get_all_data(self):
        f = open( self.path, 'r' )
        reader = csv.DictReader( f)
        result = json.dumps( [ row for row in reader ] )
        result = json.loads(result)
        return result

    # search for any data by its key, and search value which can
    # be a string or integer
    # returns an array of all the data that matches the search field and
    # its relating row / information
    # used only once for the first time searching(!!important!!)
    def first_search(self, search_criteria, search_value):
        self.print_execution('  ⌕ Searching For ' + str(search_value) +
                             ' in All `' + search_criteria + '` Field Of Csv Data...  ')
        search_criteria_data = self.sort_data(self.data)
        result = []

        if(type(search_value).__name__ == 'list'):
            for i in range(len(search_criteria_data[search_criteria])):
                check = search_criteria_data[search_criteria][i]
                search_value[0] = self.set_data_type(check, search_value[0])
                search_value[1] = self.set_data_type(check, search_value[1])
                if check.isdigit() and check.find('.') != -1:
                    check = float(search_criteria_data[search_criteria][i])
                if(check > search_value[0] and check <= search_value[1]):
                    result.append(self.search_by_index(
                        i + 1, search_criteria_data))
            self.print_execution_completed('  ✓ Search Completed....  ')
            return result

        else:
            for i in range(len(search_criteria_data[search_criteria])):
                check = search_criteria_data[search_criteria][i]
                search_value = self.set_data_type(check, search_value)
                if(check == search_value):
                    result.append(self.search_by_index(
                        i + 1, search_criteria_data))
            self.print_execution_completed('  ✓ Search Completed....  ')
            return result

    # search for any data by its key, and search value which can
    # be a string or integer
    # returns an array of all the data that matches the search field and
    # its relating row / information
    # used only afer the first time searching(!!important!!)
    def search(self, sorted_data, search_criteria, search_value):
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
                return result
        else:
            for i in range(len(sorted_data)):
                check = sorted_data[i][search_criteria]
                search_value = self.set_data_type(check, search_value)
                if(check == search_value):
                    result.append(sorted_data[i])
            self.print_execution_completed('  ✓ Search Completed....  ')
            return result

    def contains(self, sorted_data, search_criteria, search_value):
        self.print_execution('  ⌕ Checking If ' + str(search_value) +
                             ' Is Contained In `' + search_criteria + '` Field Of Csv Data...  ')
        index = None
        result = []
        for i in range(len(sorted_data)):
            check = sorted_data[i][search_criteria]
            search_value = self.set_data_type(check, search_value)
            if(check.lower().find(search_value.lower()) != -1):
                result.append(sorted_data[i])
        self.print_execution_completed('  ✓ Search Completed....  ')
        return result

    # function find each person by index
    # returns person in that index and all data relating to that person
    def search_by_index(self, index, data):
        searchCriterias = self.return_all_criterias()
        index = index - 1
        result = {}

        for i in range(len(searchCriterias)):
            result[searchCriterias[i]] = data[searchCriterias[i]][index]

        return result

    # list of all search criterias that could be used
    def return_all_criterias(self):
        return self.headers

    # function to sort all data into a dictionary using search criterias as key
    # returns a dictionary of all search criterias with all specific data
    # in thier in thier right positions
    def sort_data(self, data_):
        self.print_execution('  📚  Sorting Data...  ')
        data = []
        trackDataKeys = {}

        for row in data_:
            data.append(row)
        constDataKeys = data[0]

        for i in range(len(data[0])):
            trackDataKeys[data[0][i]] = []
        data.pop(0)

        for i in range(len(data)):
            for j in range(len(data[i])):
                trackDataKeys[constDataKeys[j]].append(data[i][j])

        return trackDataKeys

    # returns maximum number in a sorted csv data set
    # the search_field should always be an int (important!!)
    # parameter 2 is already soreted data (important!!)
    def get_maximum_value(self, search_field, sorted_data):
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

            return result

    # returns minimum number in a sorted csv data set
    # the search_field should always be an int (important!!)
    # parameter 2 is already soreted data (important!!)
    def get_minimum_value(self, search_field, sorted_data):
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
    def print_filtered_json_tofile(self, data, name_of_file):
        self.print_execution(
            '  🖨  Printing Sorted Data To File (' + str(name_of_file) + '.json)...  ')
        directory = './filtered_data/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + name_of_file + '.json', 'w') as outfile:
            json.dump(data, outfile)

    def delete_json_file(self, filepath):
        os.remove('./filtered_data/' + filepath + '.json')

    # print list with bullet points / arrows
    def print_all_search_fields(self, message, all_search_fields):
        sorted_data = self.sort_data(self.data)
        key = None
        print(colored(message, 'grey', 'on_white', attrs=['bold']))
        print('----------------------------------------')
        for i in range(len(all_search_fields)):
            arrows = colored('⎸►| ', 'magenta')
            key = all_search_fields[i]
            length_of_field = len(sorted_data[all_search_fields[i]])
            pick_random_field = random.randint(0, length_of_field)
            print(
                arrows + colored(all_search_fields[i] + ' ➾ ' + sorted_data[all_search_fields[i]][pick_random_field], 'cyan', attrs=['bold']))
        print('----------------------------------------')
        data_len = str(len(sorted_data[key]))
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
        self.print_execution_completed('  ✓ Csv File Imported Successfully  ')
        # prints out all search fields / criterias that
        # can be used to filter the csv data imported
        message = '    Snippet Of The Data Csv Imported    '
        self.print_all_search_fields(message, self.headers)
        print('----------------------------------------')

    def send_data_as_post(self, url, data):
        if(len(data) > 0):
            self.print_execution(
                '  📩  Sending Data To The Web For Vizualization  ')
            headers = {'X-Requested-With': 'XMLHttpRequest'}
            post_data = {'mapData': json.dumps(data)}
            post = requests.post(url=url, headers=headers, data=post_data)
            return post
            self.print_execution_completed(
                '  📬  Data Sent Successfully ')

    # pretty print end of excecution time
    def end(self):
        end = time.time()
        total_time = str(round(end - self.start_time, 3))
        print('----------------------------------------')
        self.print_execution('            ⏳ Execution Time           ')
        cprint('             ' + total_time +
               ' second(s)             ', 'white', 'on_magenta')
        print('----------------------------------------')
