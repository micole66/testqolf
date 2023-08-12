import pandas as pd
from utils import load_data, save_data

DATA_PATH = "path/to/data"

def process_data():
    data = load_data(DATA_PATH)
    processed_data = data_preprocessing(data)
    save_data(processed_data, DATA_PATH)

def data_preprocessing(data):
    # Assuming the data is in pandas DataFrame format
    # Remove any null values
    data = data.dropna()

    # Convert all text to lowercase for uniformity
    data['keyword'] = data['keyword'].str.lower()

    # Remove any special characters
    data['keyword'] = data['keyword'].str.replace('[^\w\s]','')

    return data

if __name__ == "__main__":
    process_data()