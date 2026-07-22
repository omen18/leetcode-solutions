"""
Problem: Number of Squareful Arrays
LeetCode #: 996
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-squareful-arrays/

Approach: Backtracking / Hamiltonian Paths on Graph. Build adjacency graph connecting numbers whose sum is a perfect square. Use count map to handle duplicates and backtrack to find valid permutations.
Time Complexity: O(N!) in worst case, heavily restricted by perfect square adjacency constraints.
Space Complexity: O(N) for recursion stack depth and graph storage.
"""

import math
from collections import Counter
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        def is_square(val: int) -> bool:
            root = int(math.isqrt(val))
            return root * root == val
        
        adj = {x: set() for x in count}
        for x in count:
            for y in count:
                if is_square(x + y):
                    adj[x].add(y)
                    
        def backtrack(last: int, left: int) -> int:
            if left == 0:
                return 1
            
            ans = 0
            for nxt in adj[last]:
                if count[nxt] > 0:
                    count[nxt] -= 1
                    ans += backtrack(nxt, left - 1)
                    count[nxt] += 1
            return ans
        
        total = 0
        for start in count:
            count[start] -= 1
            total += backtrack(start, len(nums) - 1)
            count[start] += 1
            
        return total
