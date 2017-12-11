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
      sorted_data = Sort(path)

      find_in_data = sorted_data.get_all_data()

      second_search = sorted_data.search(find_in_data, 'state', 'MD')

      third_search = sorted_data.contains(second_search, 'neighborhood', 'Park')

      url = 'https://dataplayground-dev.herokuapp.com/data-playground'
      sorted_data.send_data_as_post(url, third_search)

      sorted_data.end()

# excecute the main function
main()
