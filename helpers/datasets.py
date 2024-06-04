import os
import json

folder_path = 'data/'

def dataset_names():
    file_list = os.listdir(folder_path)
    print(file_list)
    with open('data/datasets', 'w') as json_file:
        json.dump(file_list, json_file, indent=4)

dataset_names()