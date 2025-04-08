import unittest
from problems import _05_move_zeroes

class TestMoveZeroes(unittest.TestCase):
    def test_example(self):
        arr = [0,1,0,3,12]
        _05_move_zeroes.move_zeroes(arr)
        self.assertEqual(arr, [1,3,12,0,0])

    def test_all_zero(self):
        arr = [0,0,0]
        _05_move_zeroes.move_zeroes(arr)
        self.assertEqual(arr, [0,0,0])

    def test_no_zero(self):
        arr = [1,2,3]
        _05_move_zeroes.move_zeroes(arr)
        self.assertEqual(arr, [1,2,3])

if __name__ == '__main__':
    unittest.main()
