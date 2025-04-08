import unittest
from problems import _03_merge_sorted_arrays

class TestMergeSortedArrays(unittest.TestCase):
    def test_merge(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        _03_merge_sorted_arrays.merge_sorted_arrays(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_empty_second(self):
        nums1 = [1]
        nums2 = []
        _03_merge_sorted_arrays.merge_sorted_arrays(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

    def test_empty_first(self):
        nums1 = [0]
        nums2 = [1]
        _03_merge_sorted_arrays.merge_sorted_arrays(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

if __name__ == '__main__':
    unittest.main()
