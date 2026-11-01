from books.data import book_data
import books.utils as u

print(book_data)

u.display_books()

u.get_book()
u.add_book("Moon and Sixpense", "Maughem", 234, 1934)
u.delete_book("Moon and Sixpense")