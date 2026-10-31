import data

def display_books():
        print(f"The books are:\n{data.books}")
        
def get_book(title):
    if title in data.books:
        print(data.books[title])
    else:
        print(f"Book '{title}' not found.")
        
def add_book(title, author, pages, year):
    if title in data.books:
        print(f"Book '{title}' already exists.")
    else:
        data.books[title] = {
            "author": author,
            "pages": pages,
            "year": year
        }
        print(f"Book '{title}' has been added.")

def delete_book(title):
    if title in data.books:
        del data.books[title]
        print(f"Book '{title}' has been deleted.")
    else:
        print(f"Book '{title}' not found.")