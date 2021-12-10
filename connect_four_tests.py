import unittest

from connect_four import ConnectFour


class ConnectFourTest(unittest.TestCase):
    def setUp(self):
        self.cf = ConnectFour()

    def test_constructor_and__str__(self):
        initial_board = """| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
"""
        self.assertEqual(initial_board, str(self.cf))

    def test_add_piece(self):
        # test piece outside the board
        with self.assertRaises(ValueError):
            self.cf.add_piece(10)
        self.cf.add_piece(1)
        self.cf.add_piece(2)
        expected_board = """| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| |X|O| | | | |
---------------
"""
        self.assertEqual(expected_board, str(self.cf))

        self.cf.add_piece(1)
        self.cf.add_piece(1)
        self.cf.add_piece(1)
        self.cf.add_piece(1)
        self.cf.add_piece(1)
        expected_board = """| |X| | | | | |
---------------
| |O| | | | | |
---------------
| |X| | | | | |
---------------
| |O| | | | | |
---------------
| |X| | | | | |
---------------
| |X|O| | | | |
---------------
"""
        self.assertEqual(expected_board, str(self.cf))

        # test place a piece when column is full
        with self.assertRaises(ValueError):
            self.cf.add_piece(1)

        self.cf.add_piece(2)
        self.cf.add_piece(3)
        self.cf.add_piece(2)
        self.cf.add_piece(3)
        self.cf.add_piece(2)
        expected_board = """| |X| | | | | |
---------------
| |O| | | | | |
---------------
| |X|O| | | | |
---------------
| |O|O| | | | |
---------------
| |X|O|X| | | |
---------------
| |X|O|X| | | |
---------------
"""
        self.assertEqual(expected_board, str(self.cf))

        # test add piece when game over
        with self.assertRaises(ValueError):
            self.cf.add_piece(3)

    def test_undo(self):
        for i in range(3):
            self.cf.add_piece(0)
            self.cf.add_piece(1)
        self.cf.add_piece(0)
        expected_board = """| | | | | | | |
---------------
| | | | | | | |
---------------
|X| | | | | | |
---------------
|X|O| | | | | |
---------------
|X|O| | | | | |
---------------
|X|O| | | | | |
---------------
"""
        self.assertEqual(expected_board, str(self.cf))
        self.assertTrue(self.cf.is_game_over())
        self.cf.undo()
        expected_board = """| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
|X|O| | | | | |
---------------
|X|O| | | | | |
---------------
|X|O| | | | | |
---------------
"""
        self.assertEqual(expected_board, str(self.cf))
        self.assertFalse(self.cf.is_game_over())


