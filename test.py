import unittest
import logic
import tictactoe

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!
    def test_vertical(self):
        board = [
            ['X', None, 'O'],
            ['X', 'O', None],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
    def test_horizontal(self):
        board = [
            ['O', 'O', 'O'],
            ['X', 'X', None],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
        
    def test_horizontal_1(self):
        board = [
        ['O', 'O', 'X'],
        ['X', 'X', 'X'],
        ['O', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
    def test_no_winner(self):
        board = [
        ['O', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), None)


if __name__ == '__main__':
    unittest.main()