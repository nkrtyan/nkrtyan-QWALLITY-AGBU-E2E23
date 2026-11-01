from data import books_list
from utils import display_books, get_book, add_book, delete_book

title = input('Enter book title: ')
deleteBook = 'Eugene Onegin' # можно получать через input, но для удобства хардкод

key = 'Eugene Onegin' # этот блок можно получать через input, но для удобства хардкод
author = 'Bulgakov'
page = 480
year = 1967




display_books(books_list)
get_book(title, books_list)
add_book(key, author, page, year, books_list)
delete_book(deleteBook, books_list)
