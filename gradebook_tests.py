'''
You must implement a testing class that thoroughly tests
the methods described in gradebook.py

You do not need to implement the methods, the description given
in the comments are sufficient for creating tests
'''
import collections
import random
from unittest import TestCase

from gradebook import Gradebook


class TestGradebook(TestCase):
    """
    Test case of class Gradebook
    """
    def setUp(self):
        """
        every before time a test runs, prepare a random grade book
        :return: None
        """
        # prepare students
        self.students = []
        self.students_number = random.randint(10, 100)
        for _ in range(self.students_number):
            self.students.append(''.join([chr(ord('a') + random.randint(0, 25))
                                          for _ in range(random.randint(1, 10))]))

        # prepare a grade book
        parameters = ["CS5001", 2021, "Fall", "John Wilder", self.students]
        self.gb = Gradebook(*parameters)

        # prepare grades
        self.grades = collections.defaultdict(list)
        self.assignments_number = random.randint(5, 10)
        for student in self.students:
            assignments_grades = {}
            for _ in range(self.assignments_number):
                grade = random.randint(60, 100)
                assignments_grades[student] = grade
                self.grades[student].append(grade)
            # add assignment grades to grade book
            self.gb.add_grade(assignments_grades)

    def test_constructor(self):
        """
        Test functionality of constructor
        :return: None
        """
        parameters = ["CS5001", 2021, "Fall", "John Wilder", ["Boyang Gao", ]]

        # test functionality of constructor
        try:
            gb = Gradebook(*parameters)
        except Exception as e:
            self.assertTrue(False)

        # test wrong course name type
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[0] = 5001
            gb = Gradebook(*wrong_parameters)

        # test wrong year type
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[1] = "2021"
            gb = Gradebook(*wrong_parameters)

        # test year less than 1999
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[1] = 1999
            gb = Gradebook(*wrong_parameters)

        # test wrong semester value
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[2] = "Winter"
            gb = Gradebook(*wrong_parameters)

        # test wrong instructor type
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[3] = ["John Wilder"]
            gb = Gradebook(*wrong_parameters)

        # test wrong students type (string)
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[4] = "Boyang Gao"
            gb = Gradebook(*wrong_parameters)

        # test wrong students type (list of types other than string)
        with self.assertRaises(ValueError):
            wrong_parameters = parameters[:]
            wrong_parameters[4] = [0, 1]
            gb = Gradebook(*wrong_parameters)

    def test_average_grade(self):
        """
        Test correctness of average_grade method of Gradebook
        :return: None
        """
        # get actual average grade not replying on any method in grade book
        sum_of_grade = 0
        for student in self.grades:
            sum_of_grade += sum(self.grades[student])
        actual_average_grade = sum_of_grade / self.students_number * self.assignments_number
        # the average grades are float, need to allow minor error
        self.assertAlmostEqual(self.gb.average_grade(), actual_average_grade)

    def test_letter_grade(self):
        """
        Test correctness of letter_grade method of Gradebook
        :return: None
        """
        # test input parameter type error
        with self.assertRaises(ValueError):
            self.gb.letter_grade("10")
        # test if the assignments number less than 1
        with self.assertRaises(ValueError):
            self.gb.letter_grade(0)

        grade_scale_reference = [
            (93, "A"),
            (90, "A-"),
            (86, "B+"),
            (82, "B"),
            (77, "B-"),
            (73, "C+"),
            (69, "C"),
            (65, "C-"),
            (0, "F")
        ]

        # get actual letter grade
        actual_letter_grade = {}

        for student in self.students:
            student_avg_grade = sum(self.grades[student]) / self.assignments_number
            for grade_threshold, letter_grade in grade_scale_reference:
                if student_avg_grade > grade_threshold:
                    actual_letter_grade[student] = letter_grade
                    break

        self.assertEqual(self.gb.letter_grade(self.assignments_number), actual_letter_grade)
