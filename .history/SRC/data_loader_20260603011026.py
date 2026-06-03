import pandas as pd 
import os

def load_data (path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")