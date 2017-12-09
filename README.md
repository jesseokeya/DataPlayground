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
