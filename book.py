"""This file has the Book class that the library program uses."""


class Book:
    """A class that stores info about one book.

    Each book has a title, an author, and an ISBN.
    """

    def __init__(self, title, author, isbn):
        """Sets up a new book.

        Parameters:
            title (str): the book's title
            author (str): who wrote the book
            isbn (str): the book's ISBN number
        """
        # the underscore means these should only be used inside the class
        self._title = title
        self._author = author
        self._isbn = isbn

    def get_title(self):
        """Gives back the title of the book."""
        return self._title

    def get_author(self):
        """Gives back the author of the book."""
        return self._author

    def get_isbn(self):
        """Gives back the ISBN of the book."""
        return self._isbn

    def __str__(self):
        """Lets you print a book in a readable way.

        Returns:
            str: the title, author, and ISBN in one line
        """
        return "Title: " + self._title + ", Author: " + self._author + ", ISBN: " + self._isbn

    def get_details(self):
        """Puts the book's info into a dictionary.

        Returns:
            dict: has the title, author, and isbn
        """
        details = {
            "title": self._title,
            "author": self._author,
            "isbn": self._isbn
        }
        return details