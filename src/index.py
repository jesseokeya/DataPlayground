'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''

# import dependencies
import sort
import csv as csv
import numpy as np
import json

# execute main function
def main():
   # import csv file to be analized(data Source)
   data = csv.reader(open('../resources/bankData.csv'))
   # range of data (index at 0 is minimum, index at 1 is maximum)
   data_range = [1, 10000]

   sort.main()

   # sort data into dictionaries with access keys
   # the access keys are the criterias
   sorted_data = sort.sort_data(data)
   find_person = sort.search_by_surname('hill', sorted_data)

   # print a viewable clean version of the dictionary in json format
   print(json.dumps(find_person, indent=1))

# excecute the main function
main()
