import pandas as pd

def load_csv(file_path):
    data = pd.read_csv('Business.csv')
    return data
