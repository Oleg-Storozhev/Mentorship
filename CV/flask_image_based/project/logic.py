import json


def open_json(path_to_json):
    with open(path_to_json, 'r') as f:
        data = json.load(f)
    return data