import json
import sys
import os



def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    pretty_print_json(json_data)
