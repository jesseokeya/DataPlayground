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

   csv_file_path = config.get_csv_system_location()
   csv_file_path = csv_file_path['path']

   # import csv file to be analized(data Source)
   data = csv.reader(open(csv_file_path))


   # sort data into dictionaries with access keys
   # the access keys are the criterias
   sorted_data = sort.sort_data(data)
   search_field = sort.search('Age', sorted_data, [0, 20])
   print(json.dumps(search_field, indent=1))
   print(len(search_field))

# excecute the main function
main()
