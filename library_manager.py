"""Main program for the library manager. Runs the menu and handles the books."""

from book import Book


def add_book(library):
    """Asks the user for book info and adds the book to the library.

    Parameters:
        library (list): the list of books to add to

    Returns:
        None
    """
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")

    # only add the book if nothing was left blank
    if title == "" or author == "" or isbn == "":
        print("You need to fill in all three fields. Book wasn't added.")
    else:
        new_book = Book(title, author, isbn)
        library.append(new_book)
        print(title + " was added.")


def list_books(library):
    """Prints out every book in the library.

    Parameters:
        library (list): the list of books to print

    Returns:
        None
    """
    if len(library) == 0:
        print("There are no books in the library yet.")
    else:
        print("Here are all the books:")
        for book in library:
            print(book)  # this uses the __str__ method from the Book class


def find_book(library, query):
    """Looks for a book by title or author.

    Parameters:
        library (list): the list of books to search
        query (str): what the user typed in to search for

    Returns:
        Book: the first book that matches, or None if nothing matches
    """
    # make everything lowercase so "harry" and "Harry" both work
    query = query.lower()

    for book in library:
        title = book.get_title().lower()
        author = book.get_author().lower()

        if query == title or query == author:
            return book

    # if the loop finishes and nothing matched
    return None


def main():
    """Runs the program and keeps showing the menu until the user exits.

    Returns:
        None
    """
    my_library = []  # this list holds all the Book objects

    running = True
    while running:
        print()
        print("--- Library Menu ---")
        print("1. Add a book")
        print("2. List all books")
        print("3. Find a book")
        print("4. Exit")

        choice = input("Pick an option (1-4): ")

        if choice == "1":
            add_book(my_library)
        elif choice == "2":
            list_books(my_library)
        elif choice == "3":
            query = input("Type a title or author to search for: ")
            result = find_book(my_library, query)
            if result is None:
                print("Couldn't find a book that matches.")
            else:
                print("Found it:")
                print(result)
        elif choice == "4":
            print("Bye!")
            running = False
        else:
            print("That's not an option, try 1, 2, 3, or 4.")


# this runs the program when you start this file
main()