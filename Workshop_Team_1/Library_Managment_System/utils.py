from .lib_data import books
# import data

def display_books():
    for name in books:
        print(
            name + ", by " + books[name]["author"] + " (" + str(books[name]["year"]) + ")"
        )

def get_book(title):
    if title in books:
        return books[title]
    else:
        return None

def add_book(title, author, pages, year):
    pass

def delete_book(title):
    pass
