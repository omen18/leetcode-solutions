"""
Problem: Valid Triangle Number
LeetCode #: 611
Difficulty: Medium
Link: https://leetcode.com/problems/valid-triangle-number/

Approach: Sort array. Fix largest side `k` from index n-1 down to 2. Use two pointers `i=0` and `j=k-1`. If `nums[i] + nums[j] > nums[k]`, all pairs between `i` and `j` work with `k` (`j - i` pairs), decrement `j`. Otherwise increment `i`.
Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary
"""

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count
