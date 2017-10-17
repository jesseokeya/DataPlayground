'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''

# import dependencies
# -------------
# local directories
import sort
import config
# -------------

import csv as csv
import json

# execute main function
def main():

   # import csv file data to be used(data Source)
   data = config.get_csv_raw_data()


   # sort data into dictionaries with access keys
   # the access keys are the criterias
   sorted_data = sort.sort_data(data)
   # print(sort.display_data_as_table(sorted_data))
   search_criteria = 'Age'
   search_value = [0, 18]
   search_field = sort.search(search_criteria, sorted_data, search_value)
   print(json.dumps(search_field, indent=1))

# excecute the main function
main()
