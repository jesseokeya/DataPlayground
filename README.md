#  DataPlayground

Understanding Your Data `Version 0.0.1`
Filter Your Data In RealTime <br /> [`https://dataplayground-dev.herokuapp.com`](https://dataplayground-dev.herokuapp.com) Gets Updated
Using Websockets

## Description
Sorting, Analyzing and Vizualizing Bank Data Collected

## Documentation
```python
# specify the path of the csv data to be anlyzed
  path = '../resources/Gun_Offenders.csv'

  # sort data by search fields / criterias
  # using indexes as access points
  sorted_data = Sort(path)

  first_search = sorted_data.first_search('sex', 'Male');

  second_search = sorted_data.search(first_search, 'state', 'MD')

  third_search = sorted_data.contains(second_search, 'full_address', 'ROSALIND')

  url = 'https://dataplayground-dev.herokuapp.com/data-playground'
  sorted_data.send_data_as_post(url, third_search)


  sorted_data.end()
```

### Usage
```python

  sorted_data = Sort(path_to_csv_file)
  
  # FIRST FUNCTION
  # first_search function must be used first to start sorting csv data
  first_search(search_criteria(one of the csv headers), search_value(value your looking for))
  returns an array of dictionaries with all the data that meets the parameters inputed
  
  # SECOND FUNCTION
  search(already_filtered_down_data_with_first_search, search_criteria(one of the csv headers), search_value(value your looking for))
  returns an array of dictionaries with all the data that meets the parameters inputed
  
  # THIRD FUNCTION
  get_maximum_value([start_range, end_range], data_to_be_filtered) and get_minimum_value([start_range, end_range], data_to_be_filtered)
  returns an array of dictionaries with all the data that meets the parameters inputed
  
  # FOURTH FUNCTION
  contains(already_filtered_down_data, search_criteria(one of the csv headers), search_value(value your looking for))
  returns an array of dictionaries with all the data that meets the parameters inputed
  
  # FIFTH FUNCTION
  return_all_criterias()
  return all csv headers / search criterias
  
  # SIXTH FUNCTION
  get_all_data()
  returns all the csv data as an array dictionaries assigned to its appropriate key values
  
  # SEVENTH FUNCTION
  display_data_as_table()
  returns a tables snippet of csv data to be analyzed
  
  # EIGHT FUNCTION
  get_col_number() and get_row_number()
  returns the length of column number(search_criterias) and/or length of row number(length of all csv data imported)
  
  # NINTH FUNCTION
  print_all_search_fields(message_to_be_printed, array_of_data_with_key_values)
  prints sinppet of csv data imported
  
  # TENTH FUNCTION
  send_data_as_post(url, data_to_be_sent)
  sends data to a website endpoint as a post request also returs a status code (.status_code, .text)
  
  # ELEVENTH FUNCTION
  end()
  prints out the time / duration it took the program from the start to the point it ends execution
  
```

### Terminal Output
<img src="https://dataplayground-dev.herokuapp.com/img/terminal.png" width="350" height="450">

### Prerequisites
```
python
```

### Excecuting
```
cd src
```

And

```
python3 index.py
```
