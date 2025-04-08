# 📅 Day 01 – Arrays (DSA with Python)

Welcome to **Day 1** of the DSA journey! Today’s focus is on solving classic array problems using efficient techniques like **Kadane’s Algorithm**, brute force, and two-pointer strategies.

---

## ✅ Problems Covered

### 1. 🔢 `two_sum.py`
**Problem**: Given an array and a target, return indices of two numbers that add up to the target.  
**Concepts**: HashMap, Two-pointer (optimized from brute-force)

---

### 2. 💥 `max_subarray.py`
**Problem**: Find the contiguous subarray with the maximum sum.  
**Concepts**: Kadane’s Algorithm  
**Edge Cases**: All negative elements, single element arrays

---

### 3. 🧪 `merge_sorted_array.py`
**Problem**: Merge two sorted arrays into one sorted array (in-place).  
**Concepts**: Two-pointer, Reverse Traversal  
**Constraints**: `nums1` has extra space at the end

---

## 🧠 Key Algorithm Used

### Kadane’s Algorithm
- Tracks the max subarray sum using local/global max
- Efficient O(n) solution
- Explained in `max_subarray.py` with dry-run and comments

---

## 🚀 File Structure

```bash
Day-01/
├── README.md           
├── runner.py
├── tests/
│   └── test_day01_problems.py
    

├── problems/
│   ├── two_sum.py
│   ├── max_subarray.py
│   └── merge_sorted_array.py
