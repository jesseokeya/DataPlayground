'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''

# import dependencies
import json
import requests
from termcolor import cprint

# local directories
# -------------
from sort import Sort
# -------------

# execute main function


def main():
    print('\n')
    print('----------------------------------------')
    cprint('        ⛹  Data Playground ⛹           ', 'white', 'on_magenta')
    print('----------------------------------------')

    # specify the path of the csv data to be anlyzed
    path = '../resources/Gun_Offenders.csv'

    # more info at ` https://catalog.data.gov/dataset/gun-offenders `
    post_path = '/data-playground'

    url = 'https://dataplayground-dev.herokuapp.com'
    local_url = 'http://localhost:3000' + post_path
    url = url + post_path

    # sort data by search fields / criterias
    # using indexes as access points
    sorted_data = Sort(path)

    # prints out all search fields / criterias that
    # can be used to filter the csv data imported
    all_search_fields = sorted_data.return_all_criterias()
    message = '   Snippet Of The Data Csv Imported  '
    sorted_data.print_all_search_fields(message, all_search_fields)
    print('----------------------------------------')
    print('\n')

    # visual representation of all your data in a table
    # print(sorted_data.display_data_as_table())

    search_criteria = 'sex'
    search_value = 'Male'
    search_field = sorted_data.first_search(search_criteria, search_value)

    more_search = sorted_data.search(search_field, 'race', 'Black')

    deeper_search = sorted_data.search(more_search, 'district', 'NED')


    sorted_data.print_filtered_json_tofile(deeper_search, 'data')

    # len_of_s = str(len(deeper_search))
    # cprint('Length Of Search Is: ' + len_of_s, 'grey',
    #        'on_cyan', attrs=['bold', 'reverse'])

    if(len(deeper_search) > 0):
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        post_data = {'mapData': json.dumps(deeper_search)}
        post = requests.post(url=url, headers=headers, data=post_data)
        # local_post = requests.post(url=local_url, headers=headers, data=post_data)


# excecute the main function
main()
