import random
import unittest

from word import Word


class WordTest(unittest.TestCase):
    def test_constructor(self):
        with self.assertRaises(TypeError):
            Word(123)
        with self.assertRaises(TypeError):
            Word([111])
        with self.assertRaises(TypeError):
            Word({111: 222})
        with self.assertRaises(TypeError):
            Word(11.11)

    def test_is_palindrome(self):
        input_word = Word('helloolleh')
        self.assertTrue(input_word.is_palindrome(1))
        input_word = Word('racecarracecarracecarracecar')
        self.assertTrue(input_word.is_palindrome(1))
        self.assertTrue(input_word.is_palindrome(2))
        self.assertTrue(input_word.is_palindrome(3))
        self.assertTrue(input_word.is_palindrome(4))
        self.assertFalse(input_word.is_palindrome(5))
        input_word = Word('racear')
        self.assertFalse(input_word.is_palindrome(1))

    def test_is_repeat(self):
        input_word = Word('hello')
        with self.assertRaises(TypeError):
            input_word.is_repeat('1')
        with self.assertRaises(ValueError):
            input_word.is_repeat(1)
        self.assertFalse(input_word.is_repeat(2))

        repeated_times = random.randint(2, 100)
        input_word = Word('hello' * repeated_times)
        self.assertFalse(input_word.is_repeat(repeated_times - 1))
        self.assertTrue(input_word.is_repeat(repeated_times))
        self.assertFalse(input_word.is_repeat(repeated_times + 1))
