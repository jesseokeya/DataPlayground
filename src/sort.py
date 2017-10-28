# import dependencies
from pandas import DataFrame
import json
import os

class Sort:
    # Constructor
    def __init__(self, data):
        self.data = data;
        self.headers = data[0]

    # search for any data by its key, and search value which can
    # be a string or integer
    # returns an array of all the data that matches the search field and
    # its relating row / information
    def search(self, search_criteria, search_value):
        search_criteria_data = self.sort_data(self.data)
        index = None
        result = [];

        if(type(search_value).__name__ == 'list'):
            for i in range(len(search_criteria_data[search_criteria])):
                check = search_criteria_data[search_criteria][i]
                search_value[0] = self.set_data_type(check, search_value[0])
                search_value[1] = self.set_data_type(check, search_value[1])
                if(check >= search_value[0] and check <= search_value[1]):
                        result.append(self.search_by_index(i+1, search_criteria_data))

            return result;

        else:
            for i in range(len(search_criteria_data[search_criteria])):
                check = search_criteria_data[search_criteria][i]
                search_value = self.set_data_type(check, search_value)
                if(check == search_value):
                        result.append(self.search_by_index(i+1, search_criteria_data))

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
        data = []
        trackDataKeys = {}

        for row in data_:
            data.append(row)
        constDataKeys = data[0];

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
        maximum_num = 0
        for i in range(len(sorted_data)):
            if(sorted_data[i][search_field]):
                maximum_num = max(maximum_num, int(sorted_data[i][search_field]))

        for i in range(len(sorted_data)):
            if(int(sorted_data[i][search_field]) == maximum_num):
                result.append(sorted_data[i])

        return result;

    # returns minimum number in a sorted csv data set
    # the search_field should always be an int (important!!)
    # parameter 2 is already soreted data (important!!)
    def get_minimum_value(self, search_field, sorted_data):
        result = []
        minimum_num = int(sorted_data[0][search_field])
        index_of_minimum = -1
        for i in range(len(sorted_data)):
            if(sorted_data[i][search_field]):
                minimum_num = min(minimum_num, int(sorted_data[i][search_field]))

        for i in range(len(sorted_data)):
            if(int(sorted_data[i][search_field]) == minimum_num):
                result.append(sorted_data[i])

        return result;

    # compares two data types and converts the data type of the
    # the first parameter as the data type of the second an returns it
    def set_data_type(self, check, search_value):
        result = None
        if(type(check).__name__ == 'str'):
            result = str(search_value)
        else:
            result = int(search_value)
        return result

    # display data in a table like in excel
    def display_data_as_table(self):
        return DataFrame(self.data)

    # get number of colums
    def get_col_number(self):
        return len(self.headers)

    # get number of rows
    def get_row_number(self):
        return len(self.data)

    # print formated json data of csv infomation to a given (filename).json
    def print_filtered_json_tofile(self, data, name_of_file):
        directory = './filtered_data/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + name_of_file + '.json', 'w') as outfile:
         json.dump(data, outfile)

    # print list with bullet points / arrows
    def print_all_search_fields(self, message, all_search_fields):
        print(message);
        print('----------------------------------------')
        for i in range(len(all_search_fields)):
            print(' ', '-> ', all_search_fields[i])
