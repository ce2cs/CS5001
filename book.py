from readability import *


class Book:
    def __init__(self, isbn, title, author, publish_year, file_format, resource_path):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publish_year = publish_year
        self._format = file_format
        self._resource_path = resource_path

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_year(self):
        return self._publish_year

    def get_format(self):
        return self._format

    def get_filename(self):
        return self._resource_path

    def _open_file(self):
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
        opened_file = self._open_file()
        words_count = {}
        hythen_breaked_word_first_half = ""
        for line in opened_file.readlines():
            word = hythen_breaked_word_first_half
            hythen_breaked_word_first_half = ""
            for i in range(len(line)):
                if line[i].isalnum():
                    word += line[i]
                elif line[i] == '-' and i == len(line) - 1:
                    hythen_breaked_word_first_half = word
                elif line[i] == '-':
                    word += line[i]
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
