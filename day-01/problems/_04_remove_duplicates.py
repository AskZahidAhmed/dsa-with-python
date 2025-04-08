"""
🚫 Problem: Remove Duplicates from Sorted Array
Return new length after removing duplicates in-place.
"""

from typing import List

def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

if __name__ == "__main__":
    print("▶ Remove Duplicates")
    arr = [1, 1, 2, 2, 3]
    k = remove_duplicates(arr)
    print("Result:", arr[:k])  # [1, 2, 3]
