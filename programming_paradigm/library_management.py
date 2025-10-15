class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # available by default

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """method to add book to the list"""
        self._books.append(book)

    def check_out_book(self, title):
      """Method to to borrow a book from the list"""
      for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()

    def return_book(self, title):
        """method to return a borrowed boook"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()

    def list_available_books(self):
        """method to list all available book"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
