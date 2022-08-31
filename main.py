from connect_DB import *


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
        print("add book")
    elif option == 2:
        print("delete book")
    elif option == 3:
        print("change book location")
    elif option == 4:
        print("register new reader")
    elif option == 5:
        print("remove reader")
    elif option == 6:
        print("search book by author")
    elif option == 7:
        print("reading a book by a reader")
    elif option == 8:
        print("order all books")
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
