import unittest
from problems import _01_two_sum

class TestTwoSum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(_01_two_sum.two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_multiple_answers(self):
        result = _01_two_sum.two_sum([3, 2, 4], 6)
        self.assertIn(result, [[1, 2], [2, 1]])

    def test_no_solution(self):
        self.assertEqual(_01_two_sum.two_sum([1, 2, 3], 7), [])

if __name__ == '__main__':
    unittest.main()
