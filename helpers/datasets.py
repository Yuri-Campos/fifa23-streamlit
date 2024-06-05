import os
import json

folder_path = 'data/datasets/'

def dataset_names():
    files = []
    file_list = os.listdir(folder_path)
    for file in file_list:
        name, ext = os.path.splitext(file)
        files.append(name)
    print(files)
    with open('data/json/datasets.json', 'w') as json_file:
        json.dump(files, json_file, indent=4)


def json_to_list():
    with open('data/json/datasets.json', 'r') as json_file:
        data = json.load(json_file)
    return list(data)


dataset_names()