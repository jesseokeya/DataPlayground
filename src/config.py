import csv as csv

def get_csv_system_location():
    csv_file_path = {}

    csv_file_path['path'] = '../resources/bank_data_uk.csv'

    return csv_file_path

def get_csv_column_headers():
    data = []
    result = None

    csv_data = csv.reader(open(get_csv_system_location()['path']))

    for row in csv_data:
        data.append(row)

    return data;
