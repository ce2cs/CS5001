from unittest import TestCase

from book import Book


class TestBook(TestCase):
    def setUp(self) -> None:
        self.book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", 1957,
                         "Hardcover", "college.txt")

    def test_constructor(self):
        with self.assertRaises(ValueError):
            book = Book("97803948000", "Cat in the Hat", "Dr. Suess", 1957,
                        "Hardcover", "college.txt")
        with self.assertRaises(ValueError):
            book = Book("a" * 13, "Cat in the Hat", "Dr. Suess", 1957,
                        "Hardcover", "college.txt")
        with self.assertRaises(ValueError):
            book = Book("9780394800011", 1123, "Dr. Suess", 1957,
                        "Hardcover", "college.txt")
        with self.assertRaises(ValueError):
            book = Book("9780394800011", "Cat in the Hat", 123123, 1957,
                        "Hardcover", "college.txt")
        with self.assertRaises(ValueError):
            book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", "sdsd",
                        "Hardcover", "college.txt")
        with self.assertRaises(ValueError):
            book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", 1957,
                        "Hardcover1", "college.txt")
        with self.assertRaises(ValueError):
            book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", 1957,
                        "Hardcover", "college1.txt")

    def test_get_title(self):
        self.assertEqual(self.book.get_title(), "Cat in the Hat")

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), "Dr. Suess")

    def test_get_year(self):
        self.assertEqual(self.book.get_year(), 1957)

    def test_get_format(self):
        self.assertEqual(self.book.get_format(), "Hardcover")

    def test_get_filename(self):
        self.assertEqual(self.book.get_filename(), "college.txt")

    def test_get_readability_grade(self):
        pass

    def test_get_index(self):
        word_dict = self.book.get_index()
        print(word_dict)
