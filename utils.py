import json


def read_json_file(path):
    with open(path, "r") as read_file:
        data = json.load(read_file)
    return data
