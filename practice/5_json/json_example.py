import json

# parse data from string to dict
data = '{"key1": 1, "key2": "2", "key3": [1, 2, 3]}'

parsed_data = json.loads(data)

print(type(parsed_data))
print(parsed_data['key1'] + 1)
print(type(parsed_data['key3']))

print("\n--------------------------------------------\n")

# converting data from dict to string
data_dict = {'key': 1, 1: 'one', 'list': [1, 2, 3]}

parsed_to_string_data = json.dumps(data_dict)

print(parsed_to_string_data)
print(type(parsed_to_string_data))
