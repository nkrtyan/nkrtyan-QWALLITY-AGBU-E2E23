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

# def get_book(title):
#     for key, value in data.books.items():
#         if key == title:
#             return value
#     return None


def add_book(title, author, pages, year):
    books[title] = {
        "author": author,
        "pages": pages,
        "year": year
    }

def delete_book(title):
    if title in books:
        del books[title]
    else: 
        print("Book not found.")

def print_separator(length):
    print("_" * length)
