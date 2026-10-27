# src/data_loader.py
import pandas as pd
import os

def load_raw_data():
    path = 'data/raw/ai4i_2020_predictive_maintenance.csv'
    if os.path.exists(path):
        df = pd.read_csv(path)
        print("Data loaded successfully!")
        return df
    else:
        print("Error: File not found. Check your directory path.")
        return None

if __name__ == "__main__":
    load_raw_data()