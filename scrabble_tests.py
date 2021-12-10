import collections
import random
import unittest

from scrabble import store_words, get_words, get_scores


class ScrabbleTest(unittest.TestCase):

    def test_store_words(self):
        expected = collections.defaultdict(list)
        words = []
        for i in range(100):
            length = random.randint(1, 10)
            word = ''.join([chr(ord('a') + random.randint(0, 25))
                            for _ in range(length)])
            words.append(word)
            expected[length].append(word)
        self.assertEqual(expected, store_words(words))

    def test_get_words(self):
        words_dict = collections.defaultdict(list)
        actual = []
        for i in range(100):
            length = random.randint(1, 10)
            word = ''.join([chr(ord('a') + random.randint(0, 25))
                            for _ in range(length)])
            words_dict[length].append(word)
            if 'a' in word and 'b' in word and length <= 6:
                actual.append(word)

        expected = get_words(6, words_dict, 'ab')

        self.assertEqual(actual, expected)

    def test_get_scores(self):
        expected = collections.defaultdict(list)
        words = []
        character_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
                            'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
                            'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
                            'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
                            'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
        for i in range(100):
            length = random.randint(1, 10)
            word = ''.join([chr(ord('a') + random.randint(0, 25))
                            for _ in range(length)])
            words.append(word)
            score = 0
            for c in word:
                score += character_values[c]
            expected[score].append(word)

        actual = get_scores(words)
        self.assertEqual(actual, expected)
