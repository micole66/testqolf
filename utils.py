import json

DATA_PATH = "data.json"

class Data:
    def __init__(self, data):
        self.data = data

def load_data():
    with open(DATA_PATH, 'r') as file:
        data = json.load(file)
    return Data(data)

def save_data(data):
    with open(DATA_PATH, 'w') as file:
        json.dump(data.data, file)