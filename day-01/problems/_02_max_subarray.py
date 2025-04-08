"""
💥 Problem: Maximum Subarray (Kadane's Algorithm)
Find the contiguous subarray with the largest sum.
"""

from typing import List

def max_subarray(nums: List[int]) -> int:
    current_sum = max_sum = nums[0]
    for n in nums[1:]:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    print("Max Subarray Sum:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print("Max Subarray Sum:", max_subarray([5,4,-1,7,8]))             # Output: 23
    print("Max Subarray Sum:", max_subarray([-1,-2,-3]))               # Output: -1
