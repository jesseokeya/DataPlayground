'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''

# import dependencies
import csv as csv
import numpy as np
import json

# execute main function
def main():
   # import csv file to be analized(data Source)
   data = csv.reader(open('../resources/bankData.csv'))
   # range of data (index at 0 is minimum, index at 1 is maximum)
   data_range = [1, 10000]
   # list of all search criterias that could be used
   searchCriterias = [
       'CustomerId',
       'Surname',
       'CreditScore',
       'Geography',
       'Gender',
       'Age',
       'Tenure',
       'Balance',
       'NumOfProducts',
       'HasCrCard',
       'IsActiveMember',
       'EstimatedSalary',
       'Exited'
       ]
   # sort data into dictionaries with access keys
   # the access keys are the criterias
   sorted_data = sort_data(data)
   find_person = search_by_surname('Obinna', sorted_data, searchCriterias)

   # print a viewable clean version of the dictionary in json format
   print(json.dumps(find_person, indent=1))

# function to sort all of the data by the users surname given
# returns a dictionary of all data related to that person
def search_by_surname(name, data, searchCriterias):
    result = None
    index = -1

    for i in range(len(data['Surname'])):
        if(data['Surname'][i].lower() == name.lower()):
            index = i + 1
            result = search_by_index(index, data, searchCriterias)
            return result

    return result;

# function find each person by index
# returns person in that index and all data relating to that person
def search_by_index(index, data, searchCriterias):
    index = index - 1
    result = {}

    for i in range(len(searchCriterias)):
        result[searchCriterias[i]] = data[searchCriterias[i]][index]

    return result

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


# excecute the main function
main()
