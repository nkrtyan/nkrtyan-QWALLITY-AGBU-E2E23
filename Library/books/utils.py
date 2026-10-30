from .data import books_info
def display_books():
    print(books_info)

def get_book(title):
    for title in books_info:
        print(title)

def add_book(title, author, page, year):
    if title not in books_info:
        books_info[title] = {
            "author": author,
            "page of nubers": page,
            "year": year,
        }
        print(books_info)

    else:
        print("Already exist")

def delete_book(title):
    if title in books_info:
        books_info.pop[title]
print(books_info)