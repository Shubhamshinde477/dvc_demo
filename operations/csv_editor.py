import os
import pandas as pd
from common_operations import get_dataset_path

def filter_data_from_csv(file_name: str):
    
    file = get_dataset_path(file_name=file_name)
    with open(file) as f:
        df = pd.read_csv(f)
        df = df[
            [
            "NAME", 
            "TELEPHONE", 
            "ADDRESS", 
            "CITY", 
            "STATE",
            "ZIP", 
            "SUBTYPE", 
            "X", 
            "Y"
            ]
            ]
        df = df.rename(columns={'SUBTYPE': 'RELIGON'})
        df.to_csv('datasets/dataset.csv', index=False)

if __name__ == "__main__":
    filter_data_from_csv("dataset.csv")
