from Library_Managment_System import utils as u
# import utils

u.display_books()
u.print_separator(50)

# print(u.get_book("The Great Gatsby"))
book = u.get_book("The Great Gatsby")
u.display_books()
u.print_separator(50)

u.add_book("The Great Gatsby", "F. Scott Fitzgerald", 180,1925)
u.display_books()
u.print_separator(50)

u.delete_book("The Great Gatsby")
u.display_books()
