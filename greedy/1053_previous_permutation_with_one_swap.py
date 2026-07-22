"""
Problem: Previous Permutation With One Swap
LeetCode #: 1053
Difficulty: Medium
Link: https://leetcode.com/problems/previous-permutation-with-one-swap/

Approach: Scan right to left to find first element arr[i] > arr[i+1]. Then find largest arr[j] < arr[i] to the right of i (choosing earliest index for duplicate values) and swap.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
            
        if i < 0:
            return arr
            
        max_idx = i + 1
        for j in range(i + 1, n):
            if arr[j] < arr[i] and arr[j] > arr[max_idx]:
                max_idx = j
                
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        return arr
