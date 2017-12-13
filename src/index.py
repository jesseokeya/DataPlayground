'''
    Name: Data Playground
    Aurthor: Jesse Okeya && Larry Agbana
    Version: 0.0.1
    Description: Sorting, Analyzing and Vizualizing Bank Data Collected
'''

# local directories
# -------------
from sort import Sort
# -------------

# execute main function


def main():
    # specify the path of the csv data to be anlyzed
        path = '../resources/Gun_Offenders.csv'

        # sort data by search fields / criterias
        # using indexes as access points
        sort_data = Sort(path)

        sort_data.search('state', 'MD')

        sort_data.contains('neighborhood', 'Park')

        url = 'https://dataplayground-dev.herokuapp.com/data-playground'
        sort_data.send_data_as_post(url)

        sort_data.end()

# excecute the main function
main()
