from datetime import date


class Book:
    def __init__(self):
        self.title = "",
        self.author = "",
        self.num_of_pages = 0


class Shelf:
    def __init__(self):
        self.books = [],
        self.is_shelf_full = False

    def add_book(self, book_obj):
        if len(self.books) < 5:
            self.books.append(book_obj)
        else:
            self.is_shelf_full = True

    def replace_books(self, book_num1, book_num2):
        if not self.books[book_num1-1] or not self.books[book_num2-1]:
            print("one or two book locations don't exist!")
        else:
            temp = self.books[book_num1-1]
            self.books[book_num1-1] = self.books[book_num2-1]
            self.books[book_num2-1] = temp

    def order_books(self):
        l = len(self.books)

        for i in range(l-1):
            for j in range(0, l-i-1):
                if self.books[j] > self.books[j+1]:
                    self.books[j], self.books[j +
                                              1] = self.books[j + 1], self.books[j]


class Reader:
    def __init__(self):
        self.id = 0,
        self.name = "",
        self.books = []

    def read_book(self, book_title):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")

        obj = {
            "title": book_title,
            "date": d1
        }
        self.books.append(obj)


class Library:
    def __init__(self):
        self.shelves = [],
        self.readers = []

    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if len(shelf) < 5:
                return True
        return False

    def add_new_book(self, book):

        for shelf in self.shelves:
            if len(shelf) < 5:
                shelf.append(book)

    def delete_book(self, book_title):
        for shelf in self.shelves:
            for book in shelf.books:
                pass
