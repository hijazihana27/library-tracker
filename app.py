import json

DATA_FILE = "books.json"


def print_banner():
    print("*** Welcome to Library Tracker (A & B) ***")


def load_books():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=2)


def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print(f"Added: {title} by {author}")


def add_book(title, author):
    if not title.strip():
        print("Title cannot be empty.")
        return
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print(f"Added: {title} by {author}")


def search_books(keyword):
    books = load_books()
    keyword = keyword.lower()
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]
    if not results:
        print("No matching books.")
        return
    for i, book in enumerate(results, start=1):
        print(f"{i}. {book['title']} by {book['author']}")


def remove_book(title):
    books = load_books()
    if not books:
        print("No books to remove.")
        return
    new_books = [b for b in books if b["title"].lower() != title.lower()]
    if len(new_books) == len(books):
        print("Book not found.")
        return
    save_books(new_books)
    print(f"Removed: {title}")


def search_and_remove_demo():
    print("Use search_books(keyword) and remove_book(title)")
