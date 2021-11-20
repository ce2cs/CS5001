import unittest
from unittest.mock import patch

from maze_solver import MazeSolver


class MazeSolverTestCase(unittest.TestCase):
    """
    Unittest of MazeSolver,
    Usage: python -m unittest maze_solver_tests.py
    if it shows import error, try pip install mock
    """

    @patch('builtins.input')
    def setUp(self, mock_input):
        self.ms = MazeSolver()
        mock_input.side_effect = ['maze-barrier.txt']
        self.ms.read_maze_from_file()

    @patch('builtins.input')
    def test_read_from_keyboard(self, mock_input):
        mock_input.side_effect = ['13 7',
                                  'XXXXXXXXXXXXX',
                                  'X           X',
                                  'X           X',
                                  'X           X',
                                  'X  XXXXXXX  X',
                                  'X           X',
                                  'XXXXXXEXXXXXX']
        self.ms.read_maze_from_keyboard()
        actual = [
            ['X'] * 13,
            ['X'] + [' '] * 11 + ['X'],
            ['X'] + [' '] * 11 + ['X'],
            ['X'] + [' '] * 11 + ['X'],
            ['X'] + [' '] * 2 + ['X'] * 7 + [' '] * 2 + ['X'],
            ['X'] + [' '] * 11 + ['X'],
            ['X'] * 6 + ['E'] + ['X'] * 6
        ]
        self.assertEqual(self.ms.maze, actual)

    @patch('builtins.input')
    def test_read_from_file(self, mock_input):
        mock_input.side_effect = ['maze-barrier.txt']
        actual = [
            ['X'] * 13,
            ['X'] + [' '] * 11 + ['X'],
            ['X'] + [' '] * 11 + ['X'],
            ['X'] + [' '] * 11 + ['X'],
            ['X'] + [' '] * 2 + ['X'] * 7 + [' '] * 2 + ['X'],
            ['X'] + [' '] * 11 + ['X'],
            ['X'] * 6 + ['E'] + ['X'] * 6
        ]
        self.ms.read_maze_from_file()
        self.assertEqual(self.ms.maze, actual)

    @patch('builtins.input')
    def test_find_exit(self, mock_input):
        mock_input.side_effect = ['3 6']
        actual = []
        with open("expected-path-for-maze-barrier.txt") as f:
            for line in f.readlines():
                actual.append([])
                for letter in line.strip():
                    actual[-1].append(letter)
        self.ms.find_exit()
        self.assertEqual(self.ms.path, actual)

