import unittest
from problems import _02_max_subarray

class TestMaxSubarray(unittest.TestCase):
    def test_kadane(self):
        self.assertEqual(_02_max_subarray.max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_single_element(self):
        self.assertEqual(_02_max_subarray.max_subarray([5]), 5)

    def test_all_negative(self):
        self.assertEqual(_02_max_subarray.max_subarray([-2,-3,-1,-5]), -1)

if __name__ == '__main__':
    unittest.main()
