import books as b

def display_books():
    print(b.books_name)


def get_book(title):
    if title in b.books_name:
        print(b.books_name[title])
    else:
        print("Book not found")  

def add_book(title,author,page,year):
    b.books_name[title] = {
                            "author": author,
                            "number_of_pages": page,
                            "year": year
                            }   

def delete_book(title):
    if title in b.books_name:
        del b.books_name[title]
        print("Book deleted")
    else:
        print("Book not found")


