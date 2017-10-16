
# function to sort all of the data by the users surname given
# returns a dictionary of all data related to that person
def search_by_surname(name, data):
    result = "No Customer By The Name " + name
    index = -1

    for i in range(len(data['Surname'])):
        if(data['Surname'][i].lower() == name.lower()):
            index = i + 1
            result = search_by_index(index, data)
            return result

    return result;

# function find each person by index
# returns person in that index and all data relating to that person
def search_by_index(index, data):
    searchCriterias = return_all_criterias()
    index = index - 1
    result = {}

    for i in range(len(searchCriterias)):
        result[searchCriterias[i]] = data[searchCriterias[i]][index]

    return result

# list of all search criterias that could be used
def return_all_criterias():
    searchCriterias = [
        'CustomerId', 'Surname', 'CreditScore', 'Geography',
        'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
        'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited'
        ]
    return searchCriterias

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

def main():
    print('\n')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Welcome To Data Playground')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
