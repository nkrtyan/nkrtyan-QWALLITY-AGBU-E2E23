from books import books_name

def display_books():
    print(books_name)

def get_book(title):
    if title in books_name.keys():
        print(books_name[title])
    else:
        print("Book not found")  

def add_book(title,author,page,year):
    if title not in books_name.keys():

        books_name[title] = {
                                "author": author,
                                "number_of_pages": page,
                                "year": year
                                }   
    else:
        print("Book already exits")    

def delete_book(title):
    if title in books_name.keys():
        del books_name[title]
        print("Book deleted")
    else:
        print("Book not found")


