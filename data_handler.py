import json
import os

DATA_FILE = "data.json"


def load_subjects():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_subjects(subjects):
    with open(DATA_FILE, "w") as f:
        json.dump(subjects, f, indent=4)