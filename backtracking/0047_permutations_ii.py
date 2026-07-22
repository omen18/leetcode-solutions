"""
Problem: Permutations II
LeetCode #: 47
Difficulty: Medium
Link: https://leetcode.com/problems/permutations-ii/

Approach: Backtracking on sorted input array with duplicate avoidance. Skip duplicate choices at the same position by checking if identical previous element has not been visited in the current tree level.
Time Complexity: O(N! * N)
Space Complexity: O(N) for recursion stack and visited tracking.
"""

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        visited = [False] * len(nums)
        
        def backtrack(current: List[int]) -> None:
            if len(current) == len(nums):
                result.append(list(current))
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                visited[i] = False
                
        backtrack([])
        return result
