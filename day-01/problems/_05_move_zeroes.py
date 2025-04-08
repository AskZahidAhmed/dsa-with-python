"""
Problem: Move Zeroes
Move all zeroes to the end while keeping the order of non-zero elements.
"""

from typing import List

def move_zeroes(nums: List[int]) -> None:
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1

if __name__ == "__main__":
    print("▶ Move Zeroes")
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print("Result:", arr)  # [1, 3, 12, 0, 0]
