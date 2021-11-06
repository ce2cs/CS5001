import unittest
from readability import *


class ReadabilityTest(unittest.TestCase):
    def setUp(self):
        file_names = ['college.txt', 'sixth-grade.txt', 'gettysburg.txt']
        self.file_data = []
        for file_name in file_names:
            with open(file_name, 'r') as f:
                self.file_data.append(f.readlines())

    def test_analyze_file_data(self):
        expected = [
            (1, 15, 31),
            (2, 29, 37),
            (11, 282, 400)
        ]
        for i in range(len(self.file_data)):
            self.assertEqual(analyze_file_data(self.file_data[i]), expected[i])

    def test_count_syllables(self):
        cases = [
            "Creighton",
            "University",
            "ea"
        ]
        expected = [
            2,
            5,
            1
        ]
        for i in range(len(expected)):
            self.assertEqual(count_syllables(cases[i]), expected[i])

    def test_flesch_index(self):
        cases = [
            (11, 282, 400),
            (2, 29, 37),
            (1, 15, 31)
        ]
        expected = [
            60.8,
            84.2,
            16.8
        ]
        for i in range(len(expected)):
            self.assertAlmostEqual(flesch_index(*cases[i]), expected[i], 1)

    def test_flesch_grade(self):
        cases = [
            20,
            30,
            40
        ]
        expected = [
            "College graduate",
            "College",
            "College"
        ]
        for i in range(len(expected)):
            self.assertEqual(flesch_grade(cases[i]), expected[i])
