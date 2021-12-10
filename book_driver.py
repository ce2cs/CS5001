'''
CS5001 Module 10 Lab on Classes & Objects
Author: Nolan Bock, Maria Jump, and 

This file implements a driver to the Book class that you are writing 
in this module.
'''
from book import Book


def main():
    book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", 1957,
                "Hardcover", "catinthehat.txt")

    # Print output
    print()
    print("Title:", book.get_title())
    print("Author:", book.get_author())
    print("Published in year:", book.get_year())
    print("Format:", book.get_format())
    print("Contained in file:", book.get_filename())
    print()
    print("Flesch Grade:", book.get_readability_grade())
    print("Index:")
    index = book.get_index()
    for k in index.keys():
        print("\t{} -- {:d}".format(k, index[k]))
    print()
    print("Printing book object:\n{0}".format(book))


if __name__ == '__main__':
    main()
