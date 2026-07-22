"""
Problem: Fair Distribution of Cookies
LeetCode #: 2305
Difficulty: Medium
Link: https://leetcode.com/problems/fair-distribution-of-cookies/

Approach: Backtracking. Distribute cookie bags among k children to minimize unfairness (maximum total cookies given to any single child). Apply early pruning by sorting inputs and skipping redundant empty child assignments.
Time Complexity: O(k^N) with heavy pruning.
Space Complexity: O(k + N) for tracking children sums and recursion stack.
"""

from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        children = [0] * k
        ans = float('inf')
        
        def backtrack(idx: int, max_val: int) -> None:
            nonlocal ans
            if max_val >= ans:
                return
            if idx == len(cookies):
                ans = min(ans, max_val)
                return
            
            zero_count = children.count(0)
            if len(cookies) - idx < zero_count:
                return
            
            for i in range(k):
                children[i] += cookies[idx]
                backtrack(idx + 1, max(max_val, children[i]))
                children[i] -= cookies[idx]
                if children[i] == 0:
                    break
                    
        backtrack(0, 0)
        return ans
