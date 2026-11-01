from .data import book_data

def display_books():
    print ("Books : ",book_data)

def get_book(*title):
    for title in book_data:
        print(title)

def add_book(title, auther, page, year):
    if title not in book_data:
        book_data[title]={"auther": auther,
        "page_numbers":page,
        "pub_year":year}
        print( f"'{title}' is successfully add")
    else:
        print(f"'{title}' is already in the list")
    return
add_book("Moon and Sixpense", "Maughem", 234, 1934)
print (book_data)

def delete_book(title):
    if title in book_data:
        book_data.pop(title)
        print("the book is successfully deleted")

