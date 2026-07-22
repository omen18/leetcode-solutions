"""
Problem: Patching Array
LeetCode #: 330
Difficulty: Hard
Link: https://leetcode.com/problems/patching-array/

Approach: Maintain smallest missing sum 'miss' covering range [1, miss-1]. Greedily add existing nums[i] if <= miss, else patch 'miss' itself into array.
Time Complexity: O(M + log N) where M is len(nums)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
                
        return patches
