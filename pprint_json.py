import json
import sys
import os



def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

def pretty_print_json(data):
    for st in data:
        print(st)


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    pretty_print_json(data)
