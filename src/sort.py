# import dependecies
import config
from pandas import DataFrame

# search for any data by its key, and search value which can
# be a string or integer
# returns an array of all the data that matches the search field and
# its relating row / information
def search(search_criteria, search_criteria_data, search_value):
    index = None
    result = [];
    
    if(type(search_value).__name__ == 'list'):
        for i in range(len(search_criteria_data[search_criteria])):
            check = search_criteria_data[search_criteria][i]
            search_value[0] = set_data_type(check, search_value[0])
            search_value[1] = set_data_type(check, search_value[1])
            if(check >= search_value[0] and check <= search_value[1]):
                    result.append(search_by_index(i+1, search_criteria_data))

        return result;

    else:
        for i in range(len(search_criteria_data[search_criteria])):
            check = search_criteria_data[search_criteria][i]
            search_value = set_data_type(check, search_value)
            if(check == search_value):
                    result.append(search_by_index(i+1, search_criteria_data))

        return result

# function find each person by index
# returns person in that index and all data relating to that person
def search_by_index(index, data):
    searchCriterias = return_all_criterias()
    index = index - 1
    result = {}

    for i in range(len(searchCriterias)):
        result[searchCriterias[i]] = data[searchCriterias[i]][index]

    return result

# list of all search criterias that could be used
def return_all_criterias():
    return config.get_csv_column_headers()[0]

# function to sort all data into a dictionary using search criterias as key
# returns a dictionary of all search criterias with all specific data
# in thier in thier right positions
def sort_data(data_):
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

# compares two data types and converts the data type of the
# the first parameter as the data type of the second an returns it
def set_data_type(check, search_value):
    result = None
    if(type(check).__name__ == 'str'):
        result = str(search_value)
    else:
        result = int(search_value)
    return result

# display data in a table like in excel
def display_data_as_table(data):
    return DataFrame(data)

# get number of colums
def get_col_number():
    return len(config.get_csv_column_headers()[0])

# get number of rows
def get_row_number():
    return len(config.get_csv_column_headers()) - 1
