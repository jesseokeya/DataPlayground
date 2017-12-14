'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''
# import dependencies
from random import choice
from sort import Sort
from os import listdir
from os.path import isfile, join

def main():
    csv_path = '../resources/'
    json_path = './filtered_data/'

    all_files = [f for f in listdir(csv_path) if isfile(join(csv_path, f))]
    for i in range(len(all_files)):
        if i < len(all_files):
            if '.csv' not in all_files[i]:
                del all_files[i]

    json_files = [f for f in listdir(json_path) if isfile(join(json_path, f))]
    for i in range(len(json_files)):
        if i < len(json_files):
            if '.json' not in all_files[i]:
                del json_files[i]
    print(json_files)
    path_to_csv_data = csv_path + choice(all_files)
    tests = Sort(path_to_csv_data)

    tests.print_execution('  🏃🏽‍ Running Tests ')

    all_data = tests.csv_data_to_json()
    tests.display_data_as_table()

    tests.get_col_number()
    tests.get_row_number()

    access_keys = tests.return_all_criterias()

    new_access_key = choice(access_keys)
    new_search_value = all_data[0][new_access_key]
    tests.search(new_access_key, new_search_value)

    last_access_key = choice(access_keys)
    last_search_value = all_data[0][last_access_key ]
    result = tests.contains(last_access_key, last_search_value)

    json_file_name = 'tests'
    json_to_csv = 'new_csv.csv'

    tests.print_filtered_json_tofile(json_file_name)
    tests.delete_json_file('tests')



    tests.print_execution('  ✓ All Tests Passed ')

    tests.end()

main()
