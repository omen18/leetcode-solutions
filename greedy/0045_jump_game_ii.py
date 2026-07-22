"""
Problem: Jump Game II
LeetCode #: 45
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game-ii/

Approach: Track the current reachable range end and the farthest position reachable in the next jump. Increment jumps whenever reaching the current end.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
