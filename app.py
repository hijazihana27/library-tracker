import json

DATA_FILE = "books.json"


def print_banner():
    print("=== Library Tracker ===")


def load_books():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=2)
