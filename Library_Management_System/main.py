from books import books_name #Fix Data import books.py
import utils as u 

u.display_books()

u.get_book('Harry Poter')

u.add_book('Sherlock Holmes', 'Arthur Conan Doyle', 304, 1887)
u.display_books()

u.delete_book('Sherlock Holmes')
u.display_books()