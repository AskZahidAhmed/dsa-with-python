"""
🔁 Problem: Merge Sorted Arrays
Merge nums2 into nums1 in-place, both are sorted.
"""

from typing import List

def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    nums1[:n] = nums2[:n]

if __name__ == "__main__":
    print("▶ Merge Sorted Arrays")
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    merge_sorted_arrays(arr1, 3, arr2, 3)
    print("Result:", arr1)  # [1, 2, 2, 3, 5, 6]
