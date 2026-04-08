import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    """Load expenses from the file, return an empty list if the file doesn't exist or is invalid"""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_expenses(expenses):
    """Save expenses to the file"""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)