from datetime import date


class Book:
    def __init__(self):
        self.title = "",
        self.author = "",
        self.num_of_pages = 0


class Shelf:
    def __init__(self):
        self.books = []
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
        self.id = 0
        self.name = ""
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
        self.shelves = []
        self.readers = []

    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if len(shelf) < 5:
                return True
        return False

    def add_new_book(self, book):

        for shelf in self.shelves:
            shelf.add_book(book)
            break

    def delete_book(self, book_title):
        for shelf in self.shelves:
            for book in shelf.books:
                if book.title == book_title:
                    pass

    def change_locations(self, book_title1, book_title2):
        count = 0
        for shelf in self.shelves:
            count += 1
            for i in range(len(shelf.books)):

                if shelf.books[i].title == book_title1:
                    book1 = shelf.books[i]
                    book_index1 = i
                    shelf_index1 = count

                if shelf.books[i].title == book_title2:
                    book2 = shelf.books[i]
                    book_index2 = i
                    shelf_index2 = count

        shelf[shelf_index1].books[book_index1] = book2
        shelf[shelf_index2].books[book_index2] = book1

    def change_locations_in_same_shelf(self, shelf, location1, location2):
        book1 = self.shelves[shelf-1].books[location1]
        book2 = self.shelves[shelf-1].books[location2]
        self.shelves[shelf-1].books[location1] = book2
        self.shelves[shelf-1].books[location2] = book1

    def order_books(self):
        for shelf in self.shelves:
            shelf.order_books()

    def register_reader(self, name, id):
        reader = Reader()
        reader.name = name
        reader.id = id
        self.readers.append(reader)

    def remove_reader(self, id):
        for reader in self.readers:
            if reader.id == id:
                arr = list(filter(lambda x: x.id != id, self.readers))

        self.readers = arr

    def reader_read_book(self, reader_id, book_title):
        for reader in self.readers:
            if reader.id == reader_id:
                reader.read_book(book_title)

    def search_by_author(self, author_name):
        arr = []
        for shelf in self.shelves:
            for book in shelf:
                if book.author == author_name:
                    arr.append(book.title)

        if len(arr) == 0:
            return print("There are no books of the author above")
        else:
            return arr
