class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)


library = Library()
library.add_book(Book("Javascript Programming", "Adamouh"))
library.add_book(Book("Java thProgramming", "Brian"))
library.add_book(Book("C++ Programming", "Alinda"))
library.display_books()
