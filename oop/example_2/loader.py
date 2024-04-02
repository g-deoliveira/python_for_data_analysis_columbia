import json

def load_data(path="inputs.json"):
    with open(path, "r") as f:
        data = json.load(f)
    return data["buyers"], data["sellers"]
