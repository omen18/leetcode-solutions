"""
Problem: Shopping Offers
LeetCode #: 638
Difficulty: Medium
Link: https://leetcode.com/problems/shopping-offers/

Approach: Top-down Dynamic Programming (Memoized DFS) - Try each valid special offer or purchase items individually.
Time Complexity: O(S * B^N) where S is special count, B is max item requirement, N is number of items.
Space Complexity: O(B^N) for memoization cache.
"""

from typing import List, Tuple


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        
        def dfs(curr_needs: Tuple[int, ...]) -> int:
            if curr_needs in memo:
                return memo[curr_needs]
                
            # Base cost buying items individually without any special offer
            cost = sum(n * p for n, p in zip(curr_needs, price))
            
            # Try applying each special offer
            for offer in special:
                next_needs = []
                for i in range(len(curr_needs)):
                    if offer[i] > curr_needs[i]:
                        break
                    next_needs.append(curr_needs[i] - offer[i])
                else:
                    # Valid offer
                    cost = min(cost, offer[-1] + dfs(tuple(next_needs)))
                    
            memo[curr_needs] = cost
            return cost
            
        return dfs(tuple(needs))
