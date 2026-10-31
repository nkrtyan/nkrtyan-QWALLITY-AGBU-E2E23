from utils import display_books, get_book, add_book, delete_book

choice = input("Enter your choice (display, get, add, delete): ")

if choice == "display":
    display_books()
elif choice == "get":
    title = input("Enter the title of the book you want to get: ")
    get_book(title)
elif choice == "add":
    title = input("Enter the title of the book you want to add: ")
    author = input("Enter the author of the book you want to add: ")
    pages = int(input("Enter the number of pages of the book you want to add: "))
    year = int(input("Enter the year of publication of the book you want to add: "))
    add_book(title, author, pages, year)
elif choice == "delete":
    title = input("Enter the title of the book you want to delete: ")
    delete_book(title)