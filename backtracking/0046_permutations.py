"""
Problem: Permutations
LeetCode #: 46
Difficulty: Medium
Link: https://leetcode.com/problems/permutations/

Approach: Backtracking. Build permutations recursively by keeping track of visited elements. At each step, pick an unvisited element to append to current permutation path.
Time Complexity: O(N! * N)
Space Complexity: O(N) for recursion stack and visited array.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)
        
        def backtrack(current: List[int]) -> None:
            if len(current) == len(nums):
                result.append(list(current))
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()
                    visited[i] = False
                    
        backtrack([])
        return result
