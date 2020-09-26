import json


FILE = 'json_config_data.json'


def get_json():
    with open(FILE, 'r') as json_file:
        x = json.load(json_file)
    return x


def get_browser():
    x = get_json()
    return x['browser']


def get_wait():
    x = get_json()
    return x['wait']


def get_mainurl():
    x = get_json()
    return x['mainurl']


# print(get_browser())