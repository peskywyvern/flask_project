import json


def get_people():
    with open('people.json', 'r') as file:
        return json.load(file)


def to_json(data):
    with open('people.json', 'w') as file:
        return json.dump(data, file, indent=2)

