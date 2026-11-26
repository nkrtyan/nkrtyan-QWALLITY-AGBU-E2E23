def display_books(books_list):
    print(books_list)


def get_book(title,books_list):
    if title in books_list:
         print(f'We have {title} book. Info about book {books_list[title]}') 
    else:
        print('Do not have book')


def add_book(key, author, page, year, books_list):
    if key in books_list:
        print(f'We have {key} book')
    else:
        books_list[key] = {
            'author':author,
            'page': page,
            'year': year }
        print(books_list)
  

def delete_book(title, books_list):
    if title not in books_list:
        print('It is impossible to delete a book that is not in the library.')
    else:  
        del books_list[title]
        print (books_list , f'Book {title} deleted !')
        
    
    
