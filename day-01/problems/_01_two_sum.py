"""
🔢 Problem: Two Sum
Given an array and a target, return indices of two numbers that add up to the target.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
    return []

if __name__ == "__main__":
    print("▶ Two Sum")
    result = two_sum([2, 7, 11, 15], 9)
    print("Result:", result)  # [0, 1]
