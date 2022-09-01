from connect_DB import books
from classes import *


lib = Library()
s1 = Shelf()
s1.add_book(books[0])
s1.add_book(books[1])
s2 = Shelf()
s2.add_book(books[2])
s2.add_book(books[3])
s3 = Shelf()
s3.add_book(books[4])
s3.add_book(books[5])
lib.shelves.append(s1)
lib.shelves.append(s2)
lib.shelves.append(s3)


def menu():
    print("For adding a book - Press 1.")
    print("For deleting a book - Press 2.")
    print("For changing books locations - Press 3.")
    print("For registering a new reader - Press 4.")
    print("For removing a reader - Press 5.")
    print("For searching books by author - Press 6.")
    print("For reading a book by a reader - Press 7.")
    print("For ordering all books - Press 8.")
    print("For saving all data - Press 9.")
    print("For loading data - Press 10.")
    print("For exit - Press 11.")


menu()
option = int(input("Select the desired option from the menu"))

while option != 11:
    if option == 1:
        title = input("Enter a book title")
        author = input("Enter the book's author")
        num_of_pages = input("Enter the book's number of pages")
        book = {
            "title": title,
            "author": author,
            "num_of_pages": num_of_pages
        }
        lib.add_new_book(book)
        for shelf in lib.shelves:
            for book in shelf.books:
                print(book)
    elif option == 2:
        title = input("Enter the book title you wish to delete")
        lib.delete_book(title)
    elif option == 3:
        answer = input(
            "Are the books you want to switch in the same shelf?(press y/n)")
        if answer == "n":
            title1 = input("Enter the first book's title")
            title2 = input("Enter the second book's title")
            lib.change_locations(title1, title2)
        elif answer == "y":
            shelf_num = input("Enter the shelf number")
            location1 = input("Enter the first book's location in shelf")
            location2 = input("Enter the second book's location in shelf")
            lib.change_locations_in_same_shelf(shelf_num, location1, location2)

    elif option == 4:
        name = input("Enter the new reader's name")
        id = input("Enter the new reader's ID")
        lib.register_reader(name, id)
    elif option == 5:
        id = input("Enter the reader's ID you wish to remove")
        lib.remove_reader(id)
    elif option == 6:
        author = input("Enter the author's name for searching books")
        lib.search_by_author(author)
    elif option == 7:
        id = input("Enter the reader's ID for adding a book to his list")
        title = input("Enter a book's title")
        lib.reader_read_book(id, title)
    elif option == 8:
        lib.order_books()
        print("books are ordered!")
    elif option == 9:
        print("save data")
    elif option == 10:
        print("load data")
    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("Select the desired option from the menu"))
print("Thanks for using this program. goodbye!")
