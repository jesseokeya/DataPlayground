#  DataPlayground

Understanding Your Data `Version 0.0.1`
Anytime Filter Your Data In RealTime `https://dataplayground-dev.herokuapp.com` Gets Updated
Using Websockets

## Description
Sorting, Analyzing and Vizualizing Bank Data Collected

## Documentation
```python
    # specify the path of the csv data to be anlyzed
    # more info at ` https://catalog.data.gov/dataset/gun-offenders `
    post_path = '/data-playground'

    url = 'https://dataplayground-dev.herokuapp.com'
    local_url = 'http://localhost:3000' + post_path ;
    url = url + post_path

    path = '../resources/Gun_Offenders.csv'

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

    search_criteria = 'sex'
    search_value = 'Male'
    # print(sorted_data.display_data_as_table())
    search_field = sorted_data.search(search_criteria, search_value)

    # print(json.dumps(search_field, indent=1))

    # minimum_death_cause = sorted_data.get_minimum_value('Deaths', search_field)
    # maximum_death_cause = sorted_data.get_maximum_value('Deaths', search_field)

    # get_minimum_age = sorted_data.get_minimum_value('Age', search_field)
    # get_maximum_creditscore = sorted_data.get_maximum_value(
    #     'CreditScore', search_field)
    #
    # print(' Lowest Number Of Deaths: ')
    # print(json.dumps(minimum_death_cause, indent=1))
    #
    # print(' Highest Number Of Deaths: ')
    # print(json.dumps(maximum_death_cause, indent=1))

    # Creates new folder filtered_data this is where all json
    # data is written to if you decide to write to a file
    # if(minimum_death_cause  and maximum_death_cause):
    #     final_result = minimum_death_cause + maximum_death_cause
    sorted_data.print_filtered_json_tofile(search_field, 'data')

    if(len(search_field) > 0):
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        post_data = {'mapData': json.dumps(search_field)}
        post = requests.post(url=url, headers=headers, data=post_data)
        local_post = requests.post(url=local_url, headers=headers, data=post_data)


    # print(len(search_field))


# excecute the main function
main()
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
