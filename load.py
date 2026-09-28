import json

def load(filename):
    try:
        with open(filename,"r") as file:
            records = json.load(file)
    except json.JSONDecodeError:
        records = []
    return print(records)
    
    
load("records.json")