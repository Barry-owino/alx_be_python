#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.

        :param title: The title of the book.
        :param author: The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.

        :param title: The title of the eBook.
        :param author: The author of the eBook.
        :param file_size: The file size of the eBook in MB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook, {self.file_size} MB)"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.

        :param title: The title of the printed book.
        :param author: The author of the printed book.
        :param page_count: The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (Print Book, {self.page_count} pages)"


class Library:
    def __init__(self):
        """Initializes a Library instance with an empty collection of books."""
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.

        :param book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)
