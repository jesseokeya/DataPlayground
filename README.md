#  DataPlayground

Understanding Your Data `Version 0.0.1`

## Description
Sorting, Analyzing and Vizualizing Bank Data Collected

## Documentation
```python

# specify the path of the csv data to be anlyzed
  path = '../resources/bank_data.csv'

  # sort data by search fields / criterias
  # using indexes as access points
  sorted_data = Sort(path)

  # prints out all search fields / criterias that
  # can be used to filter the csv data imported
  all_search_fields = sorted_data.return_all_criterias()
  message = ' All Search Fields In Data Imported '
  sorted_data.print_all_search_fields(message, all_search_fields)
  print('----------------------------------------')
  print('\n')

  # visual representation of all your data in a table
  # print(sorted_data.display_data_as_table())

  search_criteria = 'Gender'
  search_value = 'Male'
  search_field = sorted_data.search(search_criteria, search_value)

  # print(json.dumps(search_field, indent=1))

  get_minimum_age = sorted_data.get_minimum_value('Age', search_field)
  get_maximum_creditscore = sorted_data.get_maximum_value('CreditScore', search_field)

  print(' People With Minimum Age: ')
  print(json.dumps(get_minimum_age, indent=1))

  print(' People With Maximum Acount CreditScore: ')
  print(json.dumps(get_maximum_creditscore, indent=1))

  # Creates new folder filtered_data this is where all json
  # data is written to if you decide to write to a file
  if(get_minimum_age and get_maximum_creditscore):
      final_result = get_minimum_age + get_maximum_creditscore
  sorted_data.print_filtered_json_tofile(final_result, 'data')

# excecute the main function
```

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
