import json
import os
from common_operations import get_dataset_path

def edit_and_save_json(file_name: str):
    
    file = get_dataset_path(file_name=file_name)
    with open(file, 'r') as f:
        response = f.read()
        response = json.loads(response)
        
        for data in response["Full"]:
            del data['State']
        with open(file, 'w') as file:
            json.dump(response, file)

if __name__ == "__main__":
    edit_and_save_json("StudentJson.json")