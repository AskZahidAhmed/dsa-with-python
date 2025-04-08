import unittest
from problems import _04_remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_normal(self):
        arr = [1,1,2]
        k = _04_remove_duplicates.remove_duplicates(arr)
        self.assertEqual(arr[:k], [1,2])

    def test_no_duplicates(self):
        arr = [1,2,3]
        k = _04_remove_duplicates.remove_duplicates(arr)
        self.assertEqual(arr[:k], [1,2,3])

    def test_all_duplicates(self):
        arr = [1,1,1]
        k = _04_remove_duplicates.remove_duplicates(arr)
        self.assertEqual(arr[:k], [1])

if __name__ == '__main__':
    unittest.main()
