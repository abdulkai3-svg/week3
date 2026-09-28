# Library Manager

This is a small Python program I made for class that keeps track of books in a library. You can add books, see all the books you added, and look up a book by its title or author. I made it to practice using functions, classes, and splitting my code into different files.

## What's in here

- `book.py` has the Book class. Every book has a title, an author, and an ISBN. There are methods to get each of those, one that prints the book out nicely, and one that gives back the book's info as a dictionary.
- `library_manager.py` is the main program. It pulls in the Book class from book.py and has the functions to add books, list them, and find one. It also has the menu that keeps showing up until you pick exit.

## How to run it

1. Make sure you have Python 3.
2. Download or clone this repo.
3. Open a terminal in the project folder.
4. Type `python3 library_manager.py` (on Windows it's `python library_manager.py`).
5. Pick 1, 2, 3, or 4 from the menu.

When you search for a book you have to type the full title or the full author name, but it doesn't matter if you use caps or not.
