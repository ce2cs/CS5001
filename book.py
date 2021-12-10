import os

from readability import *


class Book:
    """
    Book class contains information of a book
    """
    def __init__(self,
                 isbn,
                 title,
                 author,
                 publish_year,
                 file_format,
                 resource_path):
        """
        Constructor
        :param isbn: ISBN, a 13-digit number starting in "978" or
        "979" that uniquely identifies the book
        :param title: a string of the book's title
        :param author: Name of the author, a string of the author's name
        :param publish_year: The year the book was published, an int
        :param file_format: The format of the book as "Hardcover",
        "Softcover", "Kindle", or "PDF"
        :param resource_path: Name of the file containing the
        text of the book, this file must exist
        """

        isbn = str(isbn)
        if len(isbn) != 13 or \
                not (isbn.startswith("978") or isbn.startswith("979")) or \
                not isbn.isnumeric():
            raise ValueError("ISBN format check failed:"
                             "Please input a 13-digit number starting "
                             "in \"978\" or \"979\"")
        self._isbn = isbn
        if type(title) != str:
            raise ValueError("Title must be a string")
        self._title = title
        if type(author) != str:
            raise ValueError("Author must be a string")
        self._author = author
        if type(publish_year) != int or publish_year > 2022:
            raise ValueError("publish year should be a valid year in Integer")
        self._publish_year = publish_year
        if file_format not in ["Hardcover", "Softcover", "Kindle", "PDF"]:
            raise ValueError("file format must be Hardcover, "
                             "Softcover, Kindle, or PDF")
        self._format = file_format
        if not os.path.exists(resource_path):
            raise ValueError("resource file not exist!")
        self._resource_path = resource_path

    def get_title(self):
        """
        Get title of the book
        :return: String
        """
        return self._title

    def get_author(self):
        """
        Get author of the book
        :return: String
        """
        return self._author

    def get_year(self):
        """
        Get author of the book
        :return: String
        """
        return self._publish_year

    def get_format(self):
        """
        Get author of the book
        :return: String
        """
        return self._format

    def get_filename(self):
        """
        Get resource path of the book
        :return: String
        """
        return self._resource_path

    def _open_file(self):
        """
        Helper function to open the resource
        :return: opened file handler
        """
        try:
            input_file = open(self.get_filename(), 'r')
            return input_file
        except FileNotFoundError:
            print(self.get_filename(), "does not exist")
        except PermissionError:
            print("You do not have sufficient permissions to open",
                  self.get_filename())
        except OSError:
            print("An unexpected error occurred while attempting to open",
                  self.get_filename())

    def get_readability_grade(self):
        """
        Get readability grade of the book
        :return: String
        """
        opened_file = self._open_file()
        # Read all of the contents of the file
        # into a list of strings called filedata.
        filedata = opened_file.readlines()
        # Analyze the data from the file to calculate
        # the number of sentences, the number of words
        # and the number of syllables in the file
        sentences, words, syllables = analyze_file_data(filedata)
        index = flesch_index(sentences, words, syllables)
        grade = flesch_grade(index)
        opened_file.close()
        return grade

    def get_index(self):
        """
        Get words count map of the book
        :return: dict
        """
        opened_file = self._open_file()
        words_count = {}
        # buffer string that stores hyphen break half word,
        # if no hyphen break word at the end of previous line,
        # it is a empty string
        hyphen_break_word_first_half = ""
        for line in opened_file.readlines():
            # concatenate previous half word and reset
            # it to empty
            word = hyphen_break_word_first_half
            hyphen_break_word_first_half = ""
            line = line.strip()
            for i in range(len(line)):
                if line[i].isalnum():
                    word += line[i].lower()
                # if last character is '-' store the first half of
                # the word
                elif line[i] == '-' and i == len(line) - 1:
                    hyphen_break_word_first_half = word
                    word = ""
                # hyphen at middle of the line will be count as
                # part of the word
                elif line[i] == '-':
                    word += line[i]
                # count the word
                elif len(word) > 0:
                    words_count[word] = words_count.setdefault(word, 0) + 1
                    word = ""
        opened_file.close()
        return words_count

    def __str__(self):
        print([self.get_title() + " by " + self.get_author(),
               str(self.get_year()) + "\nISBN: " + str(self._isbn),
               self.get_format(),
               str(self.get_readability_grade()),
               self.get_filename()
               ])
        return ", ".join([self.get_title() + " by " + self.get_author(),
                          str(self.get_year()) + "\nISBN: " + str(self._isbn),
                          self.get_format(),
                          str(self.get_readability_grade()),
                          self.get_filename()
                          ])
